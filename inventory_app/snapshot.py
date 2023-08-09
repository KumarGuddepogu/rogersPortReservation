import pandas as pd


def process_dataframe(df):
    bandwidth = ['1GE', '10GE', '100GE']

    df1 = df[['Slot', 'Module_Description']].drop_duplicates()
    slot = df1['Slot'].values.tolist()
    cards = df1['Module_Description'].values.tolist()

    # ten_u = []
    # ten_a = []
    # ten_r = []
    # ton_u = []
    # ton_a = []
    # ton_r = []
    # one_u = []
    # one_a = []
    # one_r = []
    result_data = []
    for i in slot:
        for card in cards:
            x = df[(df['Slot'] == i) & (df['Module_Description'] == card)]

            if not i:  # Handle blank or None 'Slot'
                i = "No Slot Information"
            if not card:  # Handle blank or None 'Card_Type'
                card = "No Card Information"

            row_data = [i, card]

            counts_non_zero = False

            for j in bandwidth:
                y = x[x['Bandwidth'] == j]
                s = y['Port_Status'].values.tolist()

                in_use_count = s.count('In Use')
                available_count = s.count('Available')
                reserved_count = s.count('Reserved')

                row_data.extend([in_use_count, available_count, reserved_count])

                if in_use_count != 0 or available_count != 0 or reserved_count != 0:
                    counts_non_zero = True

            if counts_non_zero:
                result_data.append(row_data)

        newdf = pd.DataFrame(result_data,
                             columns=['Slot', 'Card_Type', '1GE In_Use', '1GE Available', '1GE Reserved', '10GE In_Use',
                                      '10GE Available', '10GE Reserved', '100GE In_Use', '100GE Available',
                                      '100GE Reserved'])

    #         for j in bandwidth:
    #             if j == "1GE":
    #                 y = x.loc[x['Bandwidth'] == j]
    #                 s = y['Port_Status'].values.tolist()
    #                 one_a.append(s.count('Available'))
    #                 one_u.append(s.count('In Use'))
    #                 one_r.append(s.count('Reserved'))
    #             if j == "10GE":
    #                 y = x.loc[x['Bandwidth'] == j]
    #                 s = y['Port_Status'].values.tolist()
    #                 ten_a.append(s.count('Available'))
    #                 ten_u.append(s.count('In Use'))
    #                 ten_r.append(s.count('Reserved'))
    #             if j == "100GE":
    #                 y = x.loc[x['Bandwidth'] == j]
    #                 s = y['Port_Status'].values.tolist()
    #                 ton_a.append(s.count('Available'))
    #                 ton_u.append(s.count('In Use'))
    #                 ton_r.append(s.count('Reserved'))
    #
    # newdf = pd.DataFrame(
    #     list(zip(slot, cards, one_u, one_a, one_r, ten_u, ten_a, ten_r, ton_u, ton_a, ton_r)),
    #     columns=['Slot', 'Card_Type', '1GE In_Use', '1GE Available', '1GE Reserved', '10GE In_Use',
    #              '10GE Available', '10GE Reserved', '100GE In_Use', '100GE Available', '100GE Reserved', ])

    newdf = newdf.drop_duplicates(subset=['Slot', 'Card_Type'])

    newdf['Numeric_Slot'] = newdf['Slot'].str.extract('(\d+)').astype(float)

    newdf = newdf.sort_values(by='Numeric_Slot')  # Numerical sorting
    newdf = newdf.drop(columns=['Numeric_Slot'])  # Drop the temporary column

    totals_row = ['Total', '', newdf['1GE In_Use'].sum(), newdf['1GE Available'].sum(), newdf['1GE Reserved'].sum(),
                  newdf['10GE In_Use'].sum(), newdf['10GE Available'].sum(), newdf['10GE Reserved'].sum(),
                  newdf['100GE In_Use'].sum(), newdf['100GE Available'].sum(), newdf['100GE Reserved'].sum()]
    totals_df = pd.DataFrame([totals_row], columns=newdf.columns)

    # Concatenate the original DataFrame with the totals DataFrame
    newdf = pd.concat([newdf, totals_df], ignore_index=True)

    newdf = newdf.reset_index(drop=True)

    newdf.iloc[-1, 0] = '<center><b>Total</b></center>'  # Merge and center 'Total' in 'Slot' column
    newdf.iloc[-1, 1] = ''

    for col in newdf.columns:
        newdf.iloc[-1, newdf.columns.get_loc(col)] = f'<b>{newdf.iloc[-1, newdf.columns.get_loc(col)]}</b>'

    def format_non_zero(val):
        if isinstance(val, int) and val != 0:
            return f'<b>{val}</b>'
        return val

    # Apply the formatting function to the 'Reserved' columns
    reserved_cols = [col for col in newdf.columns if 'Reserved' in col]
    newdf[reserved_cols] = newdf[reserved_cols].applymap(format_non_zero)

    df_html = newdf.to_html(classes='my-table-class', index=False, escape=False)
    return df_html




