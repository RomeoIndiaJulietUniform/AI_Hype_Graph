import matplotlib.pyplot as plt
from pytrends.request import TrendReq

# Initialize pytrends
pytrends = TrendReq(hl='en-US', tz=360)

# Define the search terms
search_terms = ["Artificial Intelligence", "Machine Learning", "Deep Learning"]

# Build the payload
pytrends.build_payload(search_terms, timeframe='today 5-y')

# Get the interest over time
data = pytrends.interest_over_time()

# Plot the data
plt.figure(figsize=(10, 6))
for term in search_terms:
    plt.plot(data[term], label=term)

plt.title('AI Hype over Time')
plt.xlabel('Year')
plt.ylabel('Interest')
plt.legend()
plt.grid(True)
plt.savefig('ai_hype_graph.png')
plt.show()
