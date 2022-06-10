import re
def solution(word, pages):
    N = len(pages)
    word, pages = word.lower(), [p.lower() for p in pages]
    defaultScores, scores = [0]*N, [0]*N
    aLinks = [None for _ in range(N)]
    keyIdxMapper = dict()
    MAIN_REGEX = '<meta property="og:url" content="(\S*)"'
    LINK_REGEX = '<a href="(\S*)"'
    
    def initDatas():
        for n in range(N):
            defaultScores[n] = scores[n] = defaultScore(n)
            keyIdxMapper[getMainLink(n)] = n
            aLinks[n] = getALinks(n)

    def calculate():
        for n in range(N):
            for link in aLinks[n]:
                if link not in keyIdxMapper: continue
                idx = keyIdxMapper[link]
                scores[idx] += defaultScores[n] / len(aLinks[n])   
        
    def answer():
        return sorted(range(N-1, -1, -1), key=lambda n: scores[n])[-1]
        
    def defaultScore(n):
        words = re.sub("[^a-z]", ' ', pages[n]).split()
        print(words)
        return len(list(filter(lambda x: x == word, words)))
    
    def getMainLink(n):
        return re.search(MAIN_REGEX, pages[n]).group(1)

    def getALinks(n):
        return re.findall(LINK_REGEX, pages[n])
    
    # drivers
    initDatas()
    calculate()
    return answer()
