import re
import argparse
import glob
import os
import pandas as pd


def generate_data(article_id,expr_type,value,offset):#get the data in df form
    data = [{'article_id': article_id, 'expr_type': expr_type, 'value': value, 'char_offset':offset}]
    df = pd.DataFrame(data)

    return df

def get_reg_type_info(reg):#seperate regular expression type and its value
    return reg[0],reg[1]

def get_month(new_str,file_idx,df):#detailed in README.md

    reg_month = ('month',r'(((?:\s*\w+\W?\s*){0,2})(January|February|March|April|May|June|July|August|September|October|November|December),?(?:\s*\w+\W?\s*){0,3})')
    reg_month_relative_year = ('month_relative_year',r'((January|February|March|April|May|June|July|August|September|October|November|December)\s(next|this|last)\syear)')
    reg_month_day = ('month_day',r'((January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2}th)')
    reg_month_year = ('month_year',r'((January|February|March|April|May|June|July|August|September|October|November|December)\s\d{4,})')
    reg_day_month_year = ('day_month_year',r'(\d{1,2}\s(January|February|March|April|May|June|July|August|September|October|November|December),?\s*\d{4,})')
    reg_day_month = ('day_month',r'(\d{1,2}\s(January|February|March|April|May|June|July|August|September|October|November|December))')
    

    reg_type,reg_info = get_reg_type_info(reg_month)
    reg_type_1,reg_info_1 = get_reg_type_info(reg_month_relative_year)
    reg_type_2,reg_info_2 = get_reg_type_info(reg_month_day)
    reg_type_3,reg_info_3 = get_reg_type_info(reg_month_year)
    reg_type_4,reg_info_4 = get_reg_type_info(reg_day_month_year)
    reg_type_5,reg_info_5 = get_reg_type_info(reg_day_month)


    if re.search(reg_info, new_str) != None:

        for match in re.finditer(reg_info, new_str):
            

            if re.search(reg_info_1,match.group(1)) != None:
                pick = re.search(reg_info_1,match.group(1))
                
                
                data = generate_data(fr'{file_idx}.txt',reg_type_1,pick.group(0),match.start()+pick.start())
                df = pd.concat([df,data])
                continue

            elif re.search(reg_info_2,match.group(1)) != None:
                pick = re.search(reg_info_2,match.group(1))
                data = generate_data(fr'{file_idx}.txt',reg_type_2,pick.group(0),match.start()+pick.start())
                df = pd.concat([df,data])
                continue

            elif re.search(reg_info_3,match.group(1)) != None:
                pick = re.search(reg_info_3,match.group(1))
                data = generate_data(fr'{file_idx}.txt',reg_type_3,pick.group(0),match.start()+pick.start())
                df = pd.concat([df,data])
                continue

            elif re.search(reg_info_4,match.group(1)) != None:
                pick = re.search(reg_info_4,match.group(1))
                data = generate_data(fr'{file_idx}.txt',reg_type_4,pick.group(0),match.start()+pick.start())
                df = pd.concat([df,data])
                continue    

            elif re.search(reg_info_5,match.group(1)) != None:
                pick = re.search(reg_info_5,match.group(1))
                data = generate_data(fr'{file_idx}.txt',reg_type_5,pick.group(0),match.start()+pick.start())
                df = pd.concat([df,data])
                continue

            else:
                data = generate_data(fr'{file_idx}.txt',reg_type,match.group(3),match.start()+len(match.group(2)))
                df = pd.concat([df,data])
            
    else:
        return df
    return df
def get_dayof_week(new_str,file_idx,df):#detailed in README.md
    reg_dayof_week = ('dayof_week',r'(Monday|Tuesday|Wednesday|Thursday|Friday)')
    reg_type,reg_info = get_reg_type_info(reg_dayof_week)
    if re.finditer is not None:
        for match in re.finditer(reg_info, new_str):
            
            data = generate_data(fr'{file_idx}.txt',reg_type,match.group(1),match.start())
            df = pd.concat([df,data])
    else:
        return df
    return df


def get_decade(new_str,file_idx,df):#detailed in README.md

    reg_decade = ('decade',r'(((?:\s*\w+\W?\s*){0,1})(\d{4,4}s))')
    reg_part_of_decade = ('part_of_decade',r'((early|late|mid)\s(\d{4,4}s))')
    reg_type,reg_info = get_reg_type_info(reg_decade)
    reg_type_1,reg_info_1 = get_reg_type_info(reg_part_of_decade)
    
    if re.search(reg_info, new_str) != None:

        for match in re.finditer(reg_info, new_str):
            

            if re.search(reg_info_1,match.group(1)) != None:
                pick = re.search(reg_info_1,match.group(1))
                data = generate_data(fr'{file_idx}.txt',reg_type_1,pick.group(0),match.start()+pick.start())
                df = pd.concat([df,data])
            else:
                data = generate_data(fr'{file_idx}.txt',reg_type,match.group(1),match.start()+len(match.group(2)))
                df = pd.concat([df,data])
    else:
        return df
    return df

def get_year(new_str,file_idx,df):#detailed in README.md
    
    reg_year = ('year',r'(((?:\s*\w+\W?\s*){0,3})(\d{4,4}\b))')
    reg_day_month_year = ('day_month_year',r'(\d{1,2}\s(January|February|March|April|May|June|July|August|September|October|November|December),?\s*\d{4,})')
    reg_month_year = ('month_year',r'((January|February|March|April|May|June|July|August|September|October|November|December)\s\d{4,})')
    reg_quarter_of_year = ('quarter_of_year',r'((first|fourth|last|second|third)(-|\s)quarter\s(of)?\s*\d{4,4})')
    
    reg_type,reg_info = get_reg_type_info(reg_year)
    reg_type_1,reg_info_1 = get_reg_type_info(reg_day_month_year)
    reg_type_2,reg_info_2 = get_reg_type_info(reg_month_year)
    reg_type_3,reg_info_3 = get_reg_type_info(reg_quarter_of_year)
    
    if re.search(reg_info, new_str) != None:

        for match in re.finditer(reg_info, new_str):
            

            if re.search(reg_info_1,match.group(1)) != None:
                pick = re.search(reg_info_1,match.group(1))
                data = generate_data(fr'{file_idx}.txt',reg_type_1,pick.group(0),match.start()+pick.start())
                df = pd.concat([df,data])
                continue

            elif re.search(reg_info_2,match.group(1)) != None:
                pick = re.search(reg_info_2,match.group(1))
                data = generate_data(fr'{file_idx}.txt',reg_type_2,pick.group(0),match.start()+pick.start())
                df = pd.concat([df,data])
                continue

            elif re.search(reg_info_3,match.group(1)) != None:
                pick = re.search(reg_info_3,match.group(1))
                data = generate_data(fr'{file_idx}.txt',reg_type_3,pick.group(0),match.start()+pick.start())
                df = pd.concat([df,data])
                continue

            
            else:
                data = generate_data(fr'{file_idx}.txt',reg_type,match.group(3),match.start()+len(match.group(2)))
                df = pd.concat([df,data])
    else:
        return df
    return df




def get_relative_year_month_week(new_str,file_idx,df):#detailed in README.md
    
    reg_relative_year_month_week = ('relative_year_month_week',r'(((?:\s*\w+\W?\s*){0,3})((last|this|next)\s(year|month|week)))')
    reg_part_of_relative_year_month_week = ('reg_part_of_relative_year_month_week',r'((earlier|early|later?)\s(this|next|last)\s(month|week|year))')
    reg_month_relative_year = ('month_relative_year',r'((January|February|March|April|May|June|July|August|September|October|November|December)\s(next|this|last)\syear)')
    
    
    reg_type,reg_info = get_reg_type_info(reg_relative_year_month_week)
    reg_type_1,reg_info_1 = get_reg_type_info(reg_part_of_relative_year_month_week)
    reg_type_2,reg_info_2 = get_reg_type_info(reg_month_relative_year)
    
    
    if re.search(reg_info, new_str) != None:

        for match in re.finditer(reg_info, new_str):
            

            if re.search(reg_info_1,match.group(1)) != None:
                pick = re.search(reg_info_1,match.group(1))
                data = generate_data(fr'{file_idx}.txt',reg_type_1,pick.group(0),match.start()+pick.start())
                df = pd.concat([df,data])
                continue

            elif re.search(reg_info_2,match.group(1)) != None:
                pick = re.search(reg_info_2,match.group(1))
                data = generate_data(fr'{file_idx}.txt',reg_type_2,pick.group(0),match.start()+pick.start())
                df = pd.concat([df,data])
                continue

            
            else:
                data = generate_data(fr'{file_idx}.txt',reg_type,match.group(3),match.start()+len(match.group(2)))
                df = pd.concat([df,data])
    else:
        return df
    return df

def get_relative_years_months_weeks_days(new_str,file_idx,df):#detailed in README.md
    reg_relative_years_months_weeks_days = ('relative_years_months_weeks_days',r'(([tT]he)?\s(last|next)\s\d{1,2}\s(years|months|days|weeks))')
    reg_type,reg_info = get_reg_type_info(reg_relative_years_months_weeks_days)
    if re.finditer is not None:
        for match in re.finditer(reg_info, new_str):
            
            data = generate_data(fr'{file_idx}.txt',reg_type,match.group(1),match.start())
            df = pd.concat([df,data])
    else:
        return df
    return df


def main(dir_in,dir_out):

    os.chdir(dir_in)
    file_list = glob.glob('*.txt')
    
    df = pd.DataFrame(columns=['article_id','expr_type','value','char_offset'])
    for i in range (1,len(file_list)+1):
        with open(fr'{i}.txt', 'r') as f:
            new_str = " ".join(line.strip() for line in f)
            file_idx = i
            df = get_dayof_week(new_str,file_idx,df)
            df = get_month(new_str,file_idx,df)
            df = get_year(new_str,file_idx,df)
            df = get_decade(new_str,file_idx,df)
            df = get_relative_year_month_week(new_str,file_idx,df)
            df = get_relative_years_months_weeks_days(new_str,file_idx,df)
            
    os.chdir('..')
    os.chdir('..')

    df[~df.duplicated()].to_csv(dir_out,index=False)
        
            


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('output')
    
    args = parser.parse_args()
    path_in = f'{args.input}'
    path_out = f'{args.output}'
    
    main(path_in,path_out)
    
            