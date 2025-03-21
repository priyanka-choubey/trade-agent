from groq_agent import get_response
from static.basic_chart import get_chart
import sys
import argparse

if __name__ == '__main__' :

    # # Initialize parser
    # parser = argparse.ArgumentParser()
    # # Adding optional argument
    # parser.add_argument("-q", "--Query", help = "Show output for the query")
    # # Read arguments from command line
    # args = parser.parse_args()

    # query = "Summarize the top performing stock of the week."

    # if args.Query:
    #     get_response(args.Query)
    # else:
    #     get_response(query)

    
    top_10_us_stocks = [                                                                                                              
      'AAPL',  # Apple Inc.                                                                                                         ┃
      'MSFT',  # Microsoft Corporation                                                                                              ┃
      'GOOG',  # Alphabet Inc. (Google)                                                                                             
      'AMZN',  # Amazon.com Inc.                                                                                                    
      'TSLA',  # Tesla Inc.                                                                                                         
      'META',    # Meta Platforms Inc. (Facebook)                                                                                     
      'BABA',  # Alibaba Group Holding Limited                                                                                      
      'JPM',   # JPMorgan Chase & Co.                                                                                               
      'V',     # Visa Inc.                                                                                                          
      'PG',    # The Procter & Gamble Company                                                                                       
   ]

    for symbol in top_10_us_stocks :
        get_chart(symbol)