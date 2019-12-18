polls - templates - polls - index.html 으로 디렉토리를 설정한 이유:
    디렉토리 충돌을 방지하기 위해

### Class Base View 를 사용하는 이유
---
1. 코드 정리: HTTP method(GET,POST) 에 대한 코드를 if...else 문이 아닌
별도로 메소드를 만들어서 사용할 수 있다. 
2. 객체 지향 기능들 : Mixin(Multiple Inheritance) 를 사용할 수 있다. 코드의 재사용성을
향상시킬 수 있다.

### Django View 의 역사
---
처음에는 view function contract 하나만 있었다. 사용자의 HttpRequest를 보내면
Django 는 HttpResponse를 돌려줬다. 

처음에 코드를 짤때 코드들에 비슷한 패턴이 존재했는데, 함수형 generic view가 이런 반복되는 패턴의 사용을
줄이게했다.

함수형 generic view는 작은 케이스를 잘 다루긴 했지만, 더 복잡한 것들을 해야할때 문제가 생기게 된다.

클래스형 generic view는 함수형 generic view와 동일한 목적으로 생성되었다.(중복된 코드 사용을 줄이고 코딩을 더 편리하게 만들기 위해)
하지만 함수형 generic view 와 다르게 mixin 등을 사용해서 보다 더 효율적이고 유연한 코딩을 할 수 있게 해주었다.

### Class-based View 사용하기
--- 
Class-based view 는 다양한 HTTP 요청에 대해 다양한 클래스 인스턴스 메소드를 사용해서 응답하게 해준다.
```python
# function-based view로 GET 핸들링하기
from django.http import HttpResponse
def my_view(request):
    if request.method =='GET':
        return HttpResponse('result')
```

```python
# class-based view로 GET 핸들링하기
from django.http import HttpResponse
from django.views import View

class MyView(View):
    def get(self,request):
        return HttpResponse('result')
```
장고의 URL resolver 는 해당 URL을 찾을 경우 옆에 적어둔 메소드를 호출한다. **하지만 우리가 class-based view 를 사용하고 싶을 경우
옆에다가 함수 대신 클래스를 적으면 안된다. 그렇기 때문에 클래스이름.as_view() 를 사용한다**


**`as_view()` 클래스 메소드는 함수를 반환하는데, 이 함수는 URL패턴이랑 일치해서 호출되는 함수와 동일하다.
이 함수는 해당 클래스의 인스턴스(객체)를 생성하고, `setup()` 메소드를 호출 해서 인스턴스를 초기화 시키고 `dispatch()` 메소드를 호출한다.
`dispatch()` 메소드는 사용자가 요청한 request 가 GET 인지 POST 인지 혹은 기타 REST API 인지 확인하고 그에 맞는 
GET 메소드 혹은 POST 메소드 등등으로 연결시켜준다. 만약에 해당 REST API에 대한 함수를 작성하지 않을 경우
`HttpResponseNotAllowed` 를 반환한다.**

Class-based view 에서 반환하는 결과는 function-based view에서 반환하는 결과랑 똑같다.
HttpResponse, redirect, HttpResponseRedirect등등..(http shortcuts 혹은 TemplateResponse)

### Mixins
---
Mixins 는 다중 상속을 의미하며 자식은 부모의 속성과 메소드를 상속받을 수 있다.

### Base View Classes
---
All views inherits form the **View** class, which handles linking the view in to the URLs,
HTTP method dispatching and other common features



#### 뷰의 종류
---
제네릭뷰란 장고에서 기본적으로 제공하고 있는 뷰의 형태로, 개발할 때 자주 등장하는 내용을 모아놓은 뷰를 뜻한다. 개발의 속도를 더욱 빠르게 만들어주어 편리하게 개발할 수 있다는 장점이 있다. 제네릭 뷰의 종류는 아래와 같다.

(1)  Base View

- View : 최상위에 있는 부모 제네릭 뷰 클래스

- Template View : 주어진 템플릿으로 렌더링해주는 뷰

- Redirect View : 주어진 URL로 Redirect해주는 기능의 뷰

 

(2)  Generic Display View

- ListView : 조건에 맞는 객체들의 목록을 보여주는 뷰

- DetailView : 조건에 맞는 하나의 세부 객체들을 보여주는 뷰

 

(3)  Generic Edit View

- FormView : 폼이 주어지면 해당 폼을 출력하는 뷰

- CreateView : 새로운 객체를 폼을 출력하는 뷰

- UpdateView : 기존의 객체를 수정하는 폼을 출력하는 뷰

- DeleteView : 기존에 있는 객체를 삭제하는 폼을 출력하는 뷰

 

(4)  Generic Date View

- YearArchiveView : 주어진 연도에 해당하는 객체를 모아줌

- MonthArchiveView : 주어진 월에 해당하는 객체를 모아줌

- DayArchiveView : 주어진 날짜에 해당하는 객체를 모아줌

- TodayArchiveView : 오늘 날짜에 해당하는 객체를 모아줌

- DateDetailView : 특정한 연, 월, 일 등에 해당하는 객체를 모아줌
   
### Generic View
---
- Each View has to know what model it will be acting upon. **This is provided using the
model attribute.**
- The DetailView generic view expects the primary key value captured from the URL to be called
**"pk".** 
    
### ListView
---
"Display a list of objects"

### DetailView
---
"Display a detail page for a particular type of object"
