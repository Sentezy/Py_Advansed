import asyncio
import aiohttp
import json



async def request_data(url):
    async with aiohttp.request('GET', url) as responce:
        return await responce.json()


async def get_reddit_top(subreddit):
    top = await request_data(f'https://www.reddit.com/r/{subreddit}/hot.json?sort=top&t=day&limit=5')

    pattern = {f'{subreddit}':{}}

    pattern[f'{subreddit}'] = {reddit.get('title'):
                                   {'score': reddit.get('score'),
                                    'link': reddit.get('url')}
                               for reddit in
                               [top['data']['children'][i]['data'] for i in range(len(top['data']['children']))]}

    return pattern


async def main():
    reddits = {
        "python",
        "compsci",
        "microbork"
    }
    res = await asyncio.gather(*(get_reddit_top(r) for r in reddits))
    return res


asyncio.run(main())
