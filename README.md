# Discord Announcer

Basically [announcement channels](https://support.discord.com/hc/articles/360032008192-), but for any text channel.

<sub>This requires client token. This can be concidered self-botting and can get your account banned.</sub>

<details>
  <summary>Installation</summary>
  
- `git clone https://github.com/c10udburst-discord/discord-announcer.git`
- create `config.json`
  - Use the [online tool](https://json.cl0udburst.ml/form/#eyIkcmVmIjoiIy9kZWZpbml0aW9ucy9Db25maWciLCJkZWZpbml0aW9ucyI6eyJDb25maWciOnsidHlwZSI6Im9iamVjdCIsImFkZGl0aW9uYWxQcm9wZXJ0aWVzIjpmYWxzZSwicHJvcGVydGllcyI6eyJ0b2tlbiI6eyJ0eXBlIjoic3RyaW5nIn0sImNoYW5uZWxzIjp7InR5cGUiOiJhcnJheSIsIml0ZW1zIjp7IiRyZWYiOiIjL2RlZmluaXRpb25zL0NoYW5uZWwifX0sImdsb2JhbHMiOnsidHlwZSI6ImFycmF5IiwiaXRlbXMiOnsiJHJlZiI6IiMvZGVmaW5pdGlvbnMvR2xvYmFsIn19fSwicmVxdWlyZWQiOlsidG9rZW4iXSwidGl0bGUiOiJDb25maWcifSwiQ2hhbm5lbCI6eyJ0eXBlIjoib2JqZWN0IiwiYWRkaXRpb25hbFByb3BlcnRpZXMiOmZhbHNlLCJwcm9wZXJ0aWVzIjp7ImlkIjp7IiRyZWYiOiIjL2RlZmluaXRpb25zL0lEIn0sIndlYmhvb2siOnsidHlwZSI6InN0cmluZyIsImV4YW1wbGVzIjpbImh0dHBzOi8vY2FuYXJ5LmRpc2NvcmQuY29tL2FwaS93ZWJob29rcy84OTI0NDgxODY2NTE0NzQzNjcvejJqMFJFcG1YTy1qV0VqbVhQalZqWlhtMHBaMm11bUtDbDJ5SjJad0ZCTGZsalp1Nl9CakxaRVFsOFp1bWpYSmZ3ciIsIjgwOTM5MTMzMzQzNTMxNTg1NC9yWGFhaFhYY1p4Wi1RbEVYalhRclhPV2xtcnVqUExsRTJPbUs0amxMbnV1dWZ1UjJYVl9XOG1tQm1QbUpyRWpydUxCSiJdfSwiZmlsdGVyIjp7IiRyZWYiOiIjL2RlZmluaXRpb25zL0ZpbHRlciJ9LCJhZGRfY2hhbm5lbCI6eyJ0eXBlIjoiYm9vbGVhbiIsImRlc2NyaXB0aW9uIjoiV2V0aGVyIG9yIG5vdCB0byBzaG93IG9yaWdpbmFsIGNoYW5uZWwgbmFtZSBpbiBtZXNzYWdlIn0sInNob3dfanVtcCI6eyJ0eXBlIjoiYm9vbGVhbiIsImRlc2NyaXB0aW9uIjoiV2V0aGVyIG9yIG5vdCB0byBzaG93IGxpbmsgdG8gb3JpZ2luYWwgbWVzc2FnZSJ9fSwicmVxdWlyZWQiOlsid2ViaG9vayIsImlkIl0sInRpdGxlIjoiQ2hhbm5lbCJ9LCJHbG9iYWwiOnsidHlwZSI6Im9iamVjdCIsImFkZGl0aW9uYWxQcm9wZXJ0aWVzIjpmYWxzZSwicHJvcGVydGllcyI6eyJmaWx0ZXIiOnsiJHJlZiI6IiMvZGVmaW5pdGlvbnMvRmlsdGVyIn0sIndlYmhvb2siOnsidHlwZSI6InN0cmluZyIsImV4YW1wbGVzIjpbImh0dHBzOi8vY2FuYXJ5LmRpc2NvcmQuY29tL2FwaS93ZWJob29rcy84OTI0NDgxODY2NTE0NzQzNjcvejJqMFJFcG1YTy1qV0VqbVhQalZqWlhtMHBaMm11bUtDbDJ5SjJad0ZCTGZsalp1Nl9CakxaRVFsOFp1bWpYSmZ3ciIsIjgwOTM5MTMzMzQzNTMxNTg1NC9yWGFhaFhYY1p4Wi1RbEVYalhRclhPV2xtcnVqUExsRTJPbUs0amxMbnV1dWZ1UjJYVl9XOG1tQm1QbUpyRWpydUxCSiJdfSwiYWRkX2NoYW5uZWwiOnsidHlwZSI6ImJvb2xlYW4iLCJkZXNjcmlwdGlvbiI6IldldGhlciBvciBub3QgdG8gc2hvdyBvcmlnaW5hbCBjaGFubmVsIG5hbWUgaW4gbWVzc2FnZSJ9LCJzaG93X2p1bXAiOnsidHlwZSI6ImJvb2xlYW4iLCJkZXNjcmlwdGlvbiI6IldldGhlciBvciBub3QgdG8gc2hvdyBsaW5rIHRvIG9yaWdpbmFsIG1lc3NhZ2UifX0sInJlcXVpcmVkIjpbImZpbHRlciIsIndlYmhvb2siXSwidGl0bGUiOiJHbG9iYWwifSwiSUQiOnsidHlwZSI6ImFycmF5IiwiaXRlbXMiOnsidHlwZSI6InN0cmluZyJ9LCJ0aXRsZSI6IklEcyJ9LCJGaWx0ZXIiOnsidHlwZSI6InN0cmluZyIsImRlc2NyaXB0aW9uIjoiUHl0aG9uIHNuaXBwZXQgdXNlZCB0byBmaWx0ZXIgbWVzc2FnZXMiLCJleGFtcGxlcyI6WyJpc19ib3QgYW5kIChub3QgaXNfd2ViaG9vaykgYW5kIGhhc19lbWJlZCIsIm1zZy5jb250ZW50LnN0YXJ0c3dpdGgoJ2JydWgnKSJdfX19=)
  OR
  - you can look at `config.example.json` look into [config.example.json](https://github.com/c10udburst-discord/discord-announcer/blob/master/config.example.json) to see how it should look
- optionally set up [venv](https://docs.python.org/3/library/venv.html)
- install requirements, by running `python3 -m pip install -r requirements.txt`
- run `main.py`

</details>
