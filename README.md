# 카나리아 : 모두를 위한 군사보안 경보기

<img src="https://cdn.pixabay.com/photo/2014/08/24/13/05/canaries-426279_960_720.jpg" width="500" height="250" alter="LOGO"/>


## 프로잭트 소개
<!--본 프로젝트는 사용자에게 보안 내용을 제거하는 기능을 가진 카메라를 제공함으로서,  
* **군 내에서 카메라를 사용 가능하게 함**과 동시에,
*  SNS에 올릴 사진의 보안 위반 가능성을 경고하여 사용자가 **자발적으로** 보안을 준수 할 수 있게 합니다. -->

### Canary?

Canary는 머신러닝을 활용하여 사진 안의 보안 위반 가능성이 있는 요소를 식별하고, 이를 사용자에게 경고해주는 통합 보안 경보 시스템입니다. 
카메라 기능과 SNS 탐지 기능으로 구성되어 있으며, 처리된 사진에는 워터마크가 들어가 처리 여부를 쉽게 식별할 수 있습니다.

### 왜 개발하게 되었는가?

* 현 실태: '국방모바일보안' 어플로 군 장병들의 카메라 사용 자체가 차단된 상황.
  * 일방적인 통제로 인한 장병들의 사기 저하
  * 추억 남기기, 부모님께 자신의 모습 보여드리기, 공익을 위한 제보 등 카메라가 있어야만 가능한 일들을 할 수 없음
  * 그러나 카메라 사용을 무턱대고 허용 시 군사기밀 등의 유출 가능성이 존재, 국가 안보에 심각한 위협이 가해질 수 있음
  * 함부로 카메라 사용을 허용할 수는 없는 상황

* Idea: 
  * 보안 위반 가능성이 있는 요소들을 식별하여 모자이크 처리를 해 주는 카메라를 만들면 될 것이다!
  * 동시에 SNS를 모니터링하여, 보안위반 가능성이 있는 사진들에 대해 게시자에게 경고해주자!
 
---

## 프로젝트 기능 설명

- Architecture


### AI



### APP

앱을 처음 실행 시, 사용자는 자신의 성명과 군번을 통해 회원가입을 진행합니다. 이 정보는 암호화되어 저장됩니다.

- **Canary Camera**(가제): 군 내부에서도 사용 가능한 카메라입니다. 촬영한 사진 안의 보안 위반 요소를 식별 후 모자이크 처리하여 반환합니다.
- **Instagram 경보기**(가제): 주요 sns 중 하나인 인스타그램 사용자의 보안 위반 여부를 탐지하고, 사용자에게 direct message로 경고해줍니다.
- ...

#### Canary Camera(가제)

<img src="sample" alter="CameraCanary"/>

사용자가 찍은 사진은 스마트폰에 바로 저장되지 않고 서버에 전송되어, 보안 위반 요소를 식별 후 적절한 강도로 모자이크 처리하여 반환됩니다.
보안 위반 요소는 사용자의 소속 부대 및 위치 식별 가능 여부, 기밀 유출 가능 여부 등을 고려하여 다음과 같이 선정하였습니다.
>총, 부대마크, 모니터, 서류, 표지판, 포, 차량, 탱크, 군용 비행기, 미사일, 항공모함  

아래 요소의 경우 촬영 당시 맥락에 따라 보안 여부가 달라지므로, 모자이크 처리는 하지 않되 사용자에게 경고문을 전달합니다.
>군복, 방탄조끼

처리된 사진이 반환될 때, 앞서 서술한 성명과 군번을 암호화한 값이 포함된 워터마크가 남습니다. 이를 이용하여 사진 처리자의 신원을 파악하거나 이미지 처리 여부를 눈으로 식별할 수 있습니다.

세부 기능은 다음과 같습니다.

- 카메라 모드: 사진을 촬영하고 서버로 전송하여 보안 위반 요소를 식별 후 적절한 강도로 모자이크 처리하여 반환됩니다.
- 갤러리 모드: 갤러리에 이미 저장된 사진을 모자이크 할 필요가 있을 시, 해당 사진을 업로드하여 카메라로 촬영할 때와 동일하게 모자이크 처리를 할 수 있습니다.
- 모자이크 강도 조절: 모자이크가 너무 강할 시 불필요한 부분까지 가릴 수 있습니다. 또는 지나치게 덜 가려서 보안 위반의 위험성이 사라지지 않을 수 있습니다. 사용자가 초기 반환 이미지의 모자이크 정도를 판단 후, 과하거나 부족하다면 강도를 약하게/세게 하여 다시 이미지를 처리합니다.

#### Instagram 경보기

<img src="sample" alter="InstagramCanary"/>

### WEB



#### (학습 자동화 기능 설명하기)


---

## 컴퓨터 구성 / 필수 조건 안내 (Prerequisites)
* ECMAScript 6 지원 브라우저 사용
* 권장: Google Chrome 버젼 77 이상

---

## 기술 스택 (Technique Used) 
### Server(back-end)
 - Node.js 기반 서버
 - express 프레임 워크 사용
 - MySQL 데이터 베이스 사용
 
### Front-end
 -  Flutter 등 사용한 front-end 프레임워크 

### AI
 - Pytorch
 - Object Detection
 - OpenCV
 - cvat.org
 - Roboflow

---

## 설치 안내 (Installation Process)
```bash
$ git clone https://github.com/osamhack2021/AI_APP_WEB_Canary_Canary
$ yarn or npm install
$ yarn start or npm run start
```

---

## 프로젝트 사용법 (Getting Started)
<!--
**마크다운 문법을 이용하여 자유롭게 기재**

잘 모를 경우
구글 검색 - 마크다운 문법
[https://post.naver.com/viewer/postView.nhn?volumeNo=24627214&memberNo=42458017](https://post.naver.com/viewer/postView.nhn?volumeNo=24627214&memberNo=42458017)

 편한 마크다운 에디터를 찾아서 사용
 샘플 에디터 [https://stackedit.io/app#](https://stackedit.io/app#)
-->

---

## 프로젝트 전망

- 장병 사기진작
군 장병들은 본 어플을 활용함으로써 군 내부에서도 위에서 언급한 것과 같이 다양한 방식으로 카메라를 사용할 수 있을 것입니다. 또한, 제한받고 있던 자유에 대한 권리를 일부 인정함으로써 장병들에 대한 대우가 점차 나아지는 것은 물론, 장병들의 사기가 오르고 그간의 속박감에서 일부 벗어나 
보다 활기차게 병영생활을 이어나갈 수 있으리라 기대됩니다.

- SNS 보안 강화
Instagram의 Canary 계정을 팔로우한 계정들의 스토리, 게시글을 스캔하며 보안 위반 요소가 없는지 지속적으로 탐지할 수 있습니다.

- 추가예정...

### 개선/발전 방향

- 타 SNS와의 연계: 현재 Instagram 계정만 지원하는 경보기 기능을 facebook 등의 타 SNS에서도 지원함으로써 보안성을 강화할 수 있습니다.
 
- 아이폰 사용자: 카메라 기능의 경우 Android용으로만 개발되었습니다. 아이폰 버전을 (~!##2%@#$^#$) 을 사용해 개발하여 더 많은 사용자가 서비스를 이용하게 할 수 있습니다.
 
- 국방모바일보안 어플 연계: 현재 카메라 차단을 담당하고 있는 해당 어플과 연계함으로써 카메라 차단/해제 기능을 활용해 사용자의 어플 강제종료를 막고, 사용성을 개선할 수 있습니다. 

- 국방인사정보체계 연계: 어플 최초 실행 시 이름과 군번을 이용해 가입한다는 점에서 착안하여, 국방인사정보체계와 연계함으로써 사용자 관리가 수월해질 것입니다. 또 해당 서버를 사용함으로써 보안 사진을 일반 서버에 저장할 때 발생할 수 있는 문제를 해결하고 보안성을 강화할 수 있습니다.

- 추가예정...

---

## 팀 정보 (Team Information)

<table>
 <tr>
  <td></td>
  <td>Name</td>
  <td>Role</td>
  <td>github</td>
  <td>e-mail</td>
 </tr>
   
 <tr>
  <td><img src="https://avatars.githubusercontent.com/u/86545225?v=4" width="50" height="50"></td>
  <td>Jaeyo Shin</td>
  <td>Leader</td>
  <td><a href="https://github.com/j-mayo"><img src="http://img.shields.io/badge/j_mayo-green?style=social&logo=github"/></a></td>
  <td><a href="mailto:tlswody5110@naver.com"><img src="https://img.shields.io/badge/tlswody5110@naver.com-green?logo=gmail&style=social"/></a></td>
 </tr>

 <tr>
  <td><img src="https://avatars.githubusercontent.com/u/76638529?v=4" width="50" height="50"></td>
  <td>June Seo</td>
  <td>Back-End (node.js)</td>
  <td><a href="https://github.com/giirafe"><img src="http://img.shields.io/badge/giirafe-green?style=social&logo=github"/></a></td>
  <td><a href="mailto:seojune408@gmail.com"><img src="https://img.shields.io/badge/seojune408@gmail.com-green?logo=gmail&style=social"/></a></td>
 </tr>
 
 <tr>
  <td><img src="https://avatars.githubusercontent.com/u/54922625?v=4" width="50" height="50"></td>
  <td>Huijae Ryu</td>
  <td>Front-End (Flutter)</td>
  <td><a href="https://github.com/hellohidi"><img src="http://img.shields.io/badge/hellohidi-green?style=social&logo=github"/></a></td>
  <td><a href="mailto:fbgmlwo123@naver.com"><img src="https://img.shields.io/badge/fbgmlwo123@naver.com-green?logo=gmail&style=social"/></a></td>
 </tr>

 <tr>
  <td><img src="https://avatars.githubusercontent.com/u/62923434?v=4" width="50" height="50"></td>
  <td>Chanho Jung</td>
  <td>Deep Learning (Pytorch)</td>
  <td><a href="https://github.com/chjung99"><img src="http://img.shields.io/badge/chjung99-green?style=social&logo=github"/></a></td>
  <td><a href="mailto:cksgh1168@gmail.com"><img src="https://img.shields.io/badge/cksgh1168@gmail.com-green?logo=gmail&style=social"/></a></td>
 </tr>

 <tr>
  <td><img src="https://avatars.githubusercontent.com/u/35412648?v=4" width="50" height="50"></td>
  <td>Donghwan Chi</td>
  <td>Deep Learning (Pytorch)</td>
  <td><a href="https://github.com/zheedong"><img src="http://img.shields.io/badge/zheedong-green?style=social&logo=github"/></a></td>
  <td><a href="mailto:zheedong@gmail.com"><img src="https://img.shields.io/badge/zheedong@gmail.com-green?logo=gmail&style=social"/></a></td>
 </tr>
   
 <tr>
  <td><img src="https://avatars.githubusercontent.com/u/40621030?v=4" width="50" height="50"></td>
  <td>Wonbeom Jang</td>
  <td>Deep Learning (Pytorch)</td>
  <td><a href="https://github.com/wonbeomjang"><img src="http://img.shields.io/badge/wonbeomjang-green?style=social&logo=github"/></a></td>
  <td><a href="mailto:jtiger958@gmail.com"><img src="https://img.shields.io/badge/jtiger958@gmail.com-green?logo=gmail&style=social"/></a></td>
 </tr>
</table>

---

## 저작권 및 사용권 정보 (Copyleft / End User License)
 * [GNU GPL](https://github.com/osamhack2021/AI_APP_WEB_Canary_Canary/blob/main/LICENSE)

This project is licensed under the terms of the GNU GPL license.
