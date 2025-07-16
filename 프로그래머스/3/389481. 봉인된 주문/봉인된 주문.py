def solution(n, bans):
    def string_to_order(s):
        """문자열을 주문서에서의 순서로 변환"""
        order = 0
        # 길이가 s보다 짧은 모든 문자열의 개수
        for length in range(1, len(s)):
            order += 26 ** length
        
        # 같은 길이에서 s보다 앞선 문자열의 개수
        for i, char in enumerate(s):
            char_index = ord(char) - ord('a')  # 0-based
            order += char_index * (26 ** (len(s) - i - 1))
        
        return order + 1  # 1-based 인덱싱
    
    def order_to_string(order):
        """순서를 문자열로 변환"""
        # 길이 찾기
        length = 1
        total = 0
        while total + 26 ** length < order:
            total += 26 ** length
            length += 1
        
        # 같은 길이에서의 인덱스 (0-based)
        index_in_length = order - total - 1
        
        # 문자열 생성
        result = ""
        for i in range(length):
            digit = index_in_length // (26 ** (length - i - 1))
            result += chr(ord('a') + digit)
            index_in_length %= (26 ** (length - i - 1))
        
        return result
    
    # 삭제된 주문들을 순서로 변환하여 정렬
    ban_orders = []
    for ban in bans:
        ban_orders.append(string_to_order(ban))
    ban_orders.sort()
    
    # n번째 주문 찾기
    current_n = n
    for ban_order in ban_orders:
        if ban_order <= current_n:
            current_n += 1
        else:
            break
    
    return order_to_string(current_n)

# 테스트
print(solution(30, ["d", "e", "bb", "aa", "ae"]))  # "ah"
print(solution(7388, ["gqk", "kdn", "jxj", "jxi", "fug", "jxg", "ewq", "len", "bhc"]))  # "jxk"