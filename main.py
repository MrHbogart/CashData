import pandas as pd

class CashData():
    def __init__(self, data_dict, n):
        self.df = pd.DataFrame.from_dict(data_dict)
        self.n = n

    def CashData(self):

        cash_date = []
        cash_price = []
        cash_volume = []
        for i in range(self.df.shape[0]%self.n, self.df.shape[0], self.n):
            sub_df = self.df[i:i + self.n]
            low_index = sub_df['low'].idxmin()
            high_index = sub_df['high'].idxmax()
            if low_index < high_index:
                cash_date.append(self.df['date'].iloc[low_index])
                cash_date.append(self.df['date'].iloc[high_index])
                cash_price.append(self.df['low'].iloc[low_index])
                cash_price.append(self.df['high'].iloc[high_index])
                cash_volume.append(self.df['volume'].iloc[low_index])
                cash_volume.append(self.df['volume'].iloc[high_index])

            elif low_index > high_index:
                cash_date.append(self.df['date'].iloc[high_index])
                cash_date.append(self.df['date'].iloc[low_index])
                cash_price.append(self.df['high'].iloc[high_index])
                cash_price.append(self.df['low'].iloc[low_index])
                cash_volume.append(self.df['volume'].iloc[high_index])
                cash_volume.append(self.df['volume'].iloc[low_index])

            else:
                if self.df['close'].iloc[low_index] > self.df['open'].iloc[low_index]:
                    cash_date.append(self.df['date'].iloc[low_index])
                    cash_date.append(self.df['date'].iloc[high_index])
                    cash_price.append(self.df['low'].iloc[low_index])
                    cash_price.append(self.df['high'].iloc[high_index])
                    cash_volume.append(self.df['volume'].iloc[low_index])
                    cash_volume.append(self.df['volume'].iloc[high_index])

                else:
                    cash_date.append(self.df['date'].iloc[high_index])
                    cash_date.append(self.df['date'].iloc[low_index])
                    cash_price.append(self.df['high'].iloc[high_index])
                    cash_price.append(self.df['low'].iloc[low_index])
                    cash_volume.append(self.df['volume'].iloc[high_index])
                    cash_volume.append(self.df['volume'].iloc[low_index])

        cash_df = pd.DataFrame(list(zip(cash_date, cash_price, cash_volume)), columns=['date', 'price', 'volume'])

        return cash_df
