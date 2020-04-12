import tstory as tistory
import chroller as chrolling
import xml.etree.ElementTree as ET
import file_handling as file_handle
import element_capture as cap

# 시간마다 반복시키기
print("Start")

# Worldometer 정보 가져오기(완료)
# chrolling.extract_links()

# 사진다운로드 받기
print("Test")
cap.capture()

# 사진올리기
# tistory.init()
# tstory.file_write()


# 블로그 올릴 내용 수정하기
# file_handle.editHTML()

#파일읽고 텍스트화 시키기.(완료)
# with open('//Users/dongjinlee/programming/js/sandbox/python/tsotry/res.html', 'r', encoding='utf-8') as file1:
#     new_content = file1.read()




#티스토리 글쓰기(완료)
# tstory.get_write(new_content)




#티스토리 직전파일 읽어오기.
# tstory.get_read()



# print(new_content)

# 티스토리 메소드
# print('list의 첫번째 글'+tstory.get_list(1))
# tstory.get_read()
# tstory.get_category()


# # 첫번째 리스트의 값 들고오기
# new_list = tistory.get_list("1")

# # 리스트에서 post id찾기
# new_post_id = new_list.json()['tistory']['item']['posts'][0]['id']

# # post id로 포스트 가져오기
# new_post = tistory.get_read(new_post_id)

# # 포스트를 XML파일로 변환하기
# root = ET.fromstring(new_post.text)
# new_post_content = ''

# # 포스트에서 Content 내용 찾기
# for content in root.iter('content'):
#     new_post_content = content.text


