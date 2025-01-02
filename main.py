from groq_agent import get_response
import sys
import argparse

# Initialize parser
parser = argparse.ArgumentParser()
# Adding optional argument
parser.add_argument("-q", "--Query", help = "Show output for the query")
# Read arguments from command line
args = parser.parse_args()

query = "Summarize the top performing stock of the week."

if args.Query:
    get_response(args.Query)
else:
    get_response(query)