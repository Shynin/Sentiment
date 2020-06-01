from textblob import TextBlob
from textPrepocessing import parsed_text
# from siteParser import text

# print(text)


# TextBlob
testimonial = TextBlob(parsed_text)
print("Text Blob")
print(testimonial.sentiment)
print(testimonial.sentiment.polarity)

# paralleldots
# import paralleldots
# paralleldots.set_api_key('API KEY')
# paralleldots.get_api_key()
# print("Parallel Dots")
# print(paralleldots.sentiment(workData))
