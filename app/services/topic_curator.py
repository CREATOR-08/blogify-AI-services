import json

from app.services.gemini import generate_response


def curate_topics(articles):

    news_text = ""

    for idx, article in enumerate(articles):

        news_text += f"""
        {idx + 1}.
        Title: {article.get("title", "")}

        Description:
        {article.get("description", "")}
        """

    prompt = f"""
You are an expert content discovery assistant for bloggers.

Analyze the news articles and select the 10 most blog-worthy topics.

Prioritize:
- Technology
- Artificial Intelligence
- Business
- Economy
- Startups
- Global Affairs
- Politics
- Climate & Sustainability

Avoid:
- Celebrity gossip
- Sports results
- Crime reports
- Local incidents
- Sensational news

For each selected topic provide:

1. title
2. summary (2-3 concise sentences explaining the news)
3. why_it_matters (why readers may care)
4. blogging_angles (3 possible perspectives a blogger can explore)

Return ONLY valid JSON.

Format:

{{
  "topics": [
    {{
      "title": "India-US Trade Agreement",
      "summary": "India and the United States are negotiating trade policies affecting tariffs and market access.",
      "why_it_matters": "The agreement could influence exports, businesses, and economic growth.",
      "blogging_angles": [
        "Economic impact",
        "Political implications",
        "Effects on businesses"
      ]
    }}
  ]
}}

News Articles:

{news_text}
"""

    response = generate_response(prompt)

    response = (
        response
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(response)