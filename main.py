def solution(s):
    answer = ''
    numbers = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    for idx,num in enumerate(numbers):
        if num in s:
            s = s.replace(num,str(idx))
            
        answer = s
    
    return int(answer)

print(solution('2three45sixseven'))