from wibuapi import WibuAPI


client = WibuAPI()


print(client.google("game of thrones"))
"""
{
  "result": [
    {
      "title": "...",
      "link": "...",
      "snippet": "...",
    }
  ],
  "success": ...,
  "creator": "Yoga Pranata"
}
"""
