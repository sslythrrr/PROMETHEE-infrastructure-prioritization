import numpy as np

class Promethee:
    def __init__(self, alternatives, criteria, weights):
        self.alternatives = alternatives
        self.criteria = criteria
        self.weights = weights
        self.n_alternatives = len(alternatives)
        self.n_criteria = len(criteria)

    def calculate_preference(self, d):
        return 1 if d > 0 else 0

    def calculate_preference_indices(self, data):
        pi = np.zeros((self.n_alternatives, self.n_alternatives))
        for i in range(self.n_alternatives):
            for j in range(self.n_alternatives):
                if i != j:
                    for k in range(self.n_criteria):
                        d = data[i][k] - data[j][k]
                        pi[i][j] += self.weights[k] * self.calculate_preference(d)
        return pi

    def calculate_flows(self, pi):
        leaving_flow = np.sum(pi, axis=1) / (self.n_alternatives - 1)
        entering_flow = np.sum(pi, axis=0) / (self.n_alternatives - 1)
        net_flow = leaving_flow - entering_flow
        return leaving_flow, entering_flow, net_flow

    def rank_alternatives(self, data):
        pi = self.calculate_preference_indices(data)
        leaving_flow, entering_flow, net_flow = self.calculate_flows(pi)
        ranking = list(zip(self.alternatives, net_flow))
        ranking.sort(key=lambda x: x[1], reverse=True)
        
        return ranking

def normalize_data(data):
    return (data - np.min(data, axis=0)) / (np.max(data, axis=0) - np.min(data, axis=0))

def promethee_ranking(alternatives, criteria_data):
    normalized_data = normalize_data(np.array(criteria_data))
    criteria = ['Biaya', 'Waktu Penyelesaian', 'Tingkat Kebutuhan', 'Dampak Sosial', 'Frekuensi Penggunaan']
    weights = [0.2, 0.2, 0.2, 0.2, 0.2]
    promethee = Promethee(alternatives, criteria, weights)
    ranking = promethee.rank_alternatives(normalized_data)
    max_net_flow = max(abs(r[1]) for r in ranking)
    results = [
        {
            'name': r[0],
            'net_flow': r[1],
            'score_percentage': (r[1] + max_net_flow) / (2 * max_net_flow) * 100
        }
        for r in ranking
    ]
    
    return results