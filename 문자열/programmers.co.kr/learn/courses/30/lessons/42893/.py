import re
def solution(word, pages):
    DB = dict()
    KEY_REG = '<meta property="og:url" content="(\S+)"'
    LINK_REG = '<a href="(https://[\S]*)"'
    word, pages = word.lower(), [p.lower() for p in pages]
    N = len(pages)
    keys, scores = [None]*N, [0]*N
    
    def initDB():        
        for idx, p in enumerate(pages):
            ds, key, links = getDefaultScore(p), getKey(p), getLinks(p)
            scores[idx], keys[idx] = ds, key
            DB[key] = {"defaultScore": ds, "links": links, "idx": idx}
                
    def linkCalculate():
        for n in range(N):
            data = DB[keys[n]]
            defaultScore, links = data["defaultScore"], data["links"]
            for link in links:
                if link not in DB: continue
                linkedIdx = DB[link]["idx"]
                scores[linkedIdx] += (defaultScore / len(links))
                
    def answer():
        result = sorted(range(N-1, -1, -1), key=lambda n: scores[n])
        return result[-1]
    
    def getDefaultScore(page):
        return re.sub('[^a-zA-Z]', ' ', page).split().count(word)
    
    def getKey(page):
        return re.search(KEY_REG, page).group(1)
    
    def getLinks(page):
        return list(re.findall(LINK_REG, page))

    initDB()
    linkCalculate()
    return answer()
