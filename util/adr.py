class Adr:
    @staticmethod
    def calculate_adr(hist):
        try:
            if len(hist) < 20:
                return None  # Not enough data to calculate ADR

            adr = 100 * (((hist['High'].iloc[0] / hist['Low'].iloc[0]) + (hist['High'].iloc[1] / hist['Low'].iloc[1]) +
                          (hist['High'].iloc[2] / hist['Low'].iloc[2]) + (hist['High'].iloc[3] / hist['Low'].iloc[3]) +
                          (hist['High'].iloc[4] / hist['Low'].iloc[4]) + (hist['High'].iloc[5] / hist['Low'].iloc[5]) +
                          (hist['High'].iloc[6] / hist['Low'].iloc[6]) + (hist['High'].iloc[7] / hist['Low'].iloc[7]) +
                          (hist['High'].iloc[8] / hist['Low'].iloc[8]) + (hist['High'].iloc[9] / hist['Low'].iloc[9]) +
                          (hist['High'].iloc[10] / hist['Low'].iloc[10]) + (
                                      hist['High'].iloc[11] / hist['Low'].iloc[11]) +
                          (hist['High'].iloc[12] / hist['Low'].iloc[12]) + (
                                      hist['High'].iloc[13] / hist['Low'].iloc[13]) +
                          (hist['High'].iloc[14] / hist['Low'].iloc[14]) + (
                                      hist['High'].iloc[15] / hist['Low'].iloc[15]) +
                          (hist['High'].iloc[16] / hist['Low'].iloc[16]) + (
                                      hist['High'].iloc[17] / hist['Low'].iloc[17]) +
                          (hist['High'].iloc[18] / hist['Low'].iloc[18]) + (
                                      hist['High'].iloc[19] / hist['Low'].iloc[19])) / 20 - 1)
            return adr
        except Exception as e:
            print(f"Error calculating ADR: {e}")
            return None
