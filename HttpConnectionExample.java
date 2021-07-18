import java.io.BufferedReader; 
import java.io.DataOutputStream; 
import java.io.InputStreamReader; 
import java.net.HttpURLConnection; 
import java.net.URL; 
import javax.net.ssl.HttpsURLConnection; 

public class HttpConnectionExample {     
    private final String USER_AGENT = "Mozilla/5.0"; 
    
    public static void main(String[] args) throws Exception { 
        int[] list = {1,2,3,3,3,4,4};
        System.out.println(cal(list));

    

        System.out.println(count);
        System.out.println("Hellow World");
        HttpConnectionExample http = new HttpConnectionExample(); 
        System.out.println("블로그 정보 API");
        http.sendGet("https://www.tistory.com/apis/blog/info?access_token=33a68a64f9a30ad458f9a21ef6007eb6_fa4950a92d3ad1a426cd0c8621a63b06&output=json");
        System.out.println();
        System.out.println("글 목록 API");
        http.sendGet("https://www.tistory.com/apis/category/list?access_token=33a68a64f9a30ad458f9a21ef6007eb6_fa4950a92d3ad1a426cd0c8621a63b06&output=json&blogName=https://digitalnomad-lee.tistory.com&page=1");
        System.out.println();
        System.out.println("카테고리 목록 API");
        http.sendGet("https://www.tistory.com/apis/category/list?access_token=33a68a64f9a30ad458f9a21ef6007eb6_fa4950a92d3ad1a426cd0c8621a63b06&output=json&blogName=https://digitalnomad-lee.tistory.com");
        System.out.println();
        System.out.println("글 읽기 API");
        http.sendGet("https://www.tistory.com/apis/post/read?access_token=33a68a64f9a30ad458f9a21ef6007eb6_fa4950a92d3ad1a426cd0c8621a63b06&output=json&blogName=https://digitalnomad-lee.tistory.com&postId=126");
        System.out.println();
        System.out.println("글 작성 API");
        String urlParameters = "access_token=33a68a64f9a30ad458f9a21ef6007eb6_fa4950a92d3ad1a426cd0c8621a63b06&output=json&blogName=https://digitalnomad-lee.tistory.com&title=test&content=test123&visibility=0&category=850377&slogan=&tag=&acceptComment=&password=";
        http.sendPost("https://www.tistory.com/apis/post/write", urlParameters); 
        //System.out.println("파일 첨부 API")
        //file_write("my_screenshot_name1")
        // http.sendGet("https://www.naver.com"); 
        //System.out.println("POST로 데이터 가져오기"); 
        // String title = "전세계 코로나 확진자 수 현황";
        // String content = "확진자 수 현황";
        // String visibility = "0" //발행상태 0비공개-기본, 1보고,3발행
        // String category_id = "850377" //카테고리 아이디 기본값 0
        // String urlParameters = "access_token=33a68a64f9a30ad458f9a21ef6007eb6_fa4950a92d3ad1a426cd0c8621a63b06&blog_name=https://digitalnomad-lee.tistory.com/&output_type=json&title=corona&content=test&visibility=0&category_id=850377"; 
        // 파일작성  API
        //String urlParameters = "access_token=33a68a64f9a30ad458f9a21ef6007eb6_fa4950a92d3ad1a426cd0c8621a63b06&output=json&blogName=https://digitalnomad-lee.tistory.com&title=test&content=test123&visibility=0&category=850377&slogan=&tag=&acceptComment=&password=";
        //String urlParameters = "sn=C02G8416DRJM&cn=&locale=&caller=&num=12345"; 
        //http.sendPost("https://www.tistory.com/apis/post/write", urlParameters); 
    } 
    // HTTP GET request 
    private void sendGet(String targetUrl) throws Exception { 
        URL url = new URL(targetUrl); 
        HttpURLConnection con = (HttpURLConnection) url.openConnection(); 
        con.setRequestMethod("GET"); // optional default is GET 
        con.setRequestProperty("User-Agent", USER_AGENT); // add request header 
        int responseCode = con.getResponseCode(); 
        BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream())); 
        String inputLine; StringBuffer response = new StringBuffer(); 
        while ((inputLine = in.readLine()) != null) { 
            response.append(inputLine); 
        } 
        in.close(); // print result 
        System.out.println("HTTP 응답 코드 : " + responseCode); 
        // System.out.println("HTTP body : " + response.toString()); 
    } 
    // HTTP POST request     
    private void sendPost(String targetUrl, String parameters) throws Exception { 
        URL url = new URL(targetUrl); 
        HttpsURLConnection con = (HttpsURLConnection) url.openConnection(); 
        con.setRequestMethod("POST"); // HTTP POST 메소드 설정
        con.setRequestProperty("User-Agent", USER_AGENT); 
        con.setDoOutput(true); // POST 파라미터 전달을 위한 설정 
        // System.out.println("1");
        // Send post request 
        DataOutputStream wr = new DataOutputStream(con.getOutputStream()); 
        wr.writeBytes(parameters); 
        wr.flush(); 
        wr.close(); 
        // System.out.println("2");
        int responseCode = con.getResponseCode(); 
        BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream())); 
        String inputLine; 
        StringBuffer response = new StringBuffer(); 
        while ((inputLine = in.readLine()) != null) { 
            response.append(inputLine); 
        } 
        in.close(); 
        // print result 
        System.out.println("HTTP 응답 코드 : " + responseCode); 
        System.out.println("HTTP body : " + response.toString());
    } 
    public int cal(int[] list){
        List countList = 0;
        for(int i =0; i<list.length(); i++){
            int count = 0;
            int num = list[i];
            for(int j = i+1; list.length(); j++){
                if(num == list[j]){
                    count++;
                }
            }
            countList.append(count);
        }
        return countList;
    }
}
