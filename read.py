class SeqRead:
    def __init__(self, read_id, seq, qualit):
        self.id = read_id
        self.seq = seq
        self.quality = qualit

    def get_seq_len(self):
        return len(self.seq)

    def get_bases_quality(self):
        d = {}
        for i in range(len(self.seq)):
            d[self.seq[i]] = self.quality[i]
        return d
