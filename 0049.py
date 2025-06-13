class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        # 정렬된 문자열을 키로 사용
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        return list(anagrams.values())
