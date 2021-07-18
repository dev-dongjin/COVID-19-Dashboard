# coding=utf-8
import requests
import webbrowser
# import file_handling as file_handle
# import chroller as chrolling


# client_id  == app_id
client_id = ""
#client_secret = Secret_Key
Secret_Key = ""
# code는 access_token을 받기 위한 중간 인증코드, 나중에 사용하지 않음.
code = ""
# access_token는 이후에 모든 인증에서 사용하는 최종 키임.
access_token = ""

# 티스토리 주소의 아이디나 전체주소
blog_name = "https://digitalnomad-lee.tistory.com/"

# 콜백주소는 자신의 티스토리 주소를 사용해도 되고, 끝에 /는 넣지 않는다.
redirect_uri = "https://digitalnomad-lee.tistory.com"
state_param = ""
output_type = "json"


def init():
    # 먼저 코드를 생성하고,
    if not code:
        auth_url = f'https://www.tistory.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code'
        webbrowser.open(auth_url)
        print('주소창에서 코드 값을 복사하세요. ?code= 이하')

    # 이후에 액세스 토큰을 받아야 한다. 이게 좀 귀찮고 낮설다.
    if not access_token:
        token_url = f'https://www.tistory.com/oauth/access_token?client_id={client_id}&client_secret={Secret_Key}&redirect_uri={redirect_uri}&code={code}&grant_type=authorization_code'
        # webbrowser.open(token_url)
        r = requests.get(token_url)
        print('r의 값은 : '+r.text)

    # 이제 실제 사용할 액세스 코드를 가지고 호출을 할 수 있다.


def get_info():
    # info_url = f'https://www.tistory.com/apis/blog/info?access_token={access_token}&output={output_type}'
    info_url = "https://www.tistory.com/apis/blog/info?access_token=33a68a64f9a30ad458f9a21ef6007eb6_fa4950a92d3ad1a426cd0c8621a63b06&output=json"
    r = requests.get(info_url)
    print(r.text)
    return r.text


def get_list(page_number):
    url = f'https://www.tistory.com/apis/post/list?access_token={access_token}&output={output_type}&blogName={blog_name}&page={page_number}'
    print(url)
    r = requests.get(url)
    print(r.text)
    return r


def get_category():
    url = f'https://www.tistory.com/apis/category/list?access_token={access_token}&output={output_type}&blogName={blog_name}'
    r = requests.get(url)
    print(r.text)
    r = r.json()['tistory']['item']['categories']
    for i in r:
        print('category의 값 가져오기')
        print(i)
        print(f'{i["name"]} ({i["id"]})')

    return r


def get_read(new_post_id):
    postid = new_post_id
    url = f'https://www.tistory.com/apis/post/read?access_token={access_token}&blogName={blog_name}&postId={postid}'
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"+url)
    r = requests.get(url)
    print(r.text)
    return(r)


# def get_write(new_content):
#     print('여기!!!!!!!!!!')
#     title = f"({chrolling.kr} 00시 기준)전세계 코로나 확진자 수 현황" #제목 (필수)
#     content = f'{new_content}'
#     visibility = "0" #발행상태 0비공개-기본, 1보고,3발행
#     category_id = "850377" #카테고리 아이디 기본값 0
#     slogan = "" #문자주소
#     tag = f"{chrolling.kr} 00시 코로나, {chrolling.kr} 00시 전세계 코로나 확진자 수 현황, {chrolling.kr} 코로나, 독일코로나, 미국코로나, 영국코로나, 이탈리아코로나, 일본코로나, 프랑스크로나, 한국코로나" #태그 ,로 구분
#     acceptComment = "" #댓글 허용 (0, 1 - 기본값)
#     password = "" #보호글 비밀번호
#     url = f'https://www.tistory.com/apis/post/write?access_token={access_token}&output={output_type}&blogName={blog_name}&title={title}&content={content}&visibility={visibility}&category={category_id}&slogan={slogan}&tag={tag}&acceptComment={acceptComment}&password={password}'
#     print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"+url)
#     r = requests.post(url)
#     print(r, r.text)
#     file_handle.saveURL(r.json()['tistory']['url'])
#     return r.json()['tistory']['url']

def file_write(capture):
    title = "테스트4"  # 제목 (필수)
    content = ''
    visibility = "0"  # 발행상태 0비공개-기본, 1보고,3발행
    category_id = "0"  # 카테고리 아이디 기본값 0
    slogan = ""  # 문자주소
    tag = ""  # 태그 ,로 구분
    files = {'uploadedfile': open(f'./data/{capture}.png', 'rb')}
    url = f'https://www.tistory.com/apis/post/attach?access_token={access_token}&blogName={blog_name}&title={title}&content={content}&visibility={visibility}&category={category_id}&slogan={slogan}&tag={tag}&output={output_type}'
    r = requests.post(url, files=files)
    print(r, r.text)
    print(r.url)
    print(r.json()['tistory']['url'])
    return r.json()['tistory']['url']
