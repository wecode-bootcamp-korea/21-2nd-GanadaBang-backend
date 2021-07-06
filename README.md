## 가나다방 프로젝트 Front-end/Back-end 소개
- 부동산 필수 앱 [다방](https://www.dabangapp.com/) 클론 프로젝트
- 짧은 프로젝트 기간동안 개발에 집중해야 하므로 디자인/기획 부분만 클론하였으며, 나머지 부분은 wecode에서 배운 내용을 활용하여 만들었습니다.
- 개발은 초기 세팅부터 전부 직접 구현했으며, 아래 데모 영상에서 보이는 부분은 모두 백앤드와 연결하여 실제 사용할 수 있는 서비스 수준으로 개발한 것입니다.
### 개발 인원 및 기간
- 개발기간 : 2021/6/7 ~ 2021/6/18
- 개발 인원
  - 프론트엔드
    - 김건우
    - 이도윤
    - 정유정
  - 백엔드
    - 김태우
    - 이아란
    - 김성규
- GitHub
  - [프론트엔드 GitHub URL](https://github.com/wecode-bootcamp-korea/21-2nd-GanadaBang-frontend)
  - [백엔드 GitHub URL](https://github.com/wecode-bootcamp-korea/21-2nd-GanadaBang-backend)
### 프로젝트 선정이유
- 외부 API를 이용한 다양한 이벤트 처리 경험
- 국내 최대 규모의 부동산 중개 어플을 모티브로 한 웹 사이트 구축 경험
- 내부의 로직을 분석하여 클론 웹 사이트에 적용
### 데모 영상
https://youtu.be/7CsPs1Z8SDY

### 적용 기술
>- Front-End : <img src="https://img.shields.io/badge/ES6+-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/React.js-61DAFB?style=for-the-badge&logo=React&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/React%20Router-CA4245?style=for-the-badge&logo=React-router&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Styled Components-CC6699?style=for-the-badge&logo=Styled-Components&logoColor=white"/>
> - Back-End : <img src="https://img.shields.io/badge/Python 3.8-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Django 3.2.4-092E20?style=for-the-badge&logo=Django&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Mysql 8.0-4479A1?style=for-the-badge&logo=Mysql&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/PyJWT 2.1-000000?style=for-the-badge&logo=JsonWebTokens&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Bcrypt 3.2-338000?style=for-the-badge&logo=PyJWT&logoColor=white"/>
> - Common : <img src="https://img.shields.io/badge/AWS RDS/EC2/S3-232F3E?style=for-the-badge&logo=Amazon&logoColor=white"/>&nbsp;
> - ETC : <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Trello-0052CC?style=for-the-badge&logo=Trello&logoColor=white"/>
#### 메인페이지
 - `search` : 모달을 조건부 렌더링과 useRef를 사용하여 input 값으로 RESTful API를 이용해 고유의 아이디가 가진 지도 페이지로 이동
 - `product list` : 렌덤한 데이터를 받아 형식에 맞게 다시 재조정하여 화면단에 보여줌
#### 회원가입 / 로그인
 - `카카오Login` : 카카오 로그인 API를 JDK로 불러와 카카오 토큰으로 활용하기
#### 상품 상세 페이지
 - `Advanced Router` : RESTfull API 파라미터 값으로 데이터 불러오기
#### 지도 페이지
 - 행정구역 검색시 리스트 응답
 - 현재 지도의 위치에 있는 매물 응답
#### 방 등록
## Reference
- 이 프로젝트는 [다방](https://www.dabangapp.com/) 사이트를 참조하여 학습목적으로 만들었습니다.
- 실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
- 이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다.
