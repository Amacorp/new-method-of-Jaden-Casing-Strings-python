def to_jaden_case(str1):
    res = []
    for i in str1.split():
        res.append(i.capitalize())
    return ' '.join(res)
    
    or
    
    # return ' '.join(i.capitalize() for i in str1.split())
    
    or

    import string
    def to_jaden_case(str1):
        return string.capwords(str1)
        
    or
    
    return " ".join(map(lambda x: x.capitalize(), string.split(' ')))

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
