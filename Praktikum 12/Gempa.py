class Gempa:
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def Dampak(self):
        if self.skala < 2:
            return "Dampak Gempanya Tidak Berasa" 
        elif 2 <= self.skala < 4:
            return "Dampak Gempanya Bangunan Retak-Retak" 
        elif 4 <= self.skala < 6:
            return "Dampak Gempanya Bangunan Roboh" 
        else:
            return "Dampak Gempanya Bangunan Roboh Dan Berpotensi Tsunami"