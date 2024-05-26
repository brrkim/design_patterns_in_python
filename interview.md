- [1. 면접](#1-면접)
  - [1.1. 공통사항](#11-공통사항)
    - [1.1.1. 2분 자기 소개해보세요](#111-2분-자기-소개해보세요)
  - [1.2. OOP Concepts](#12-oop-concepts)
    - [1.2.1. Object-Oriented Paradigm](#121-object-oriented-paradigm)
      - [1.2.1.1. 절차지향 언어의 단점?](#1211-절차지향-언어의-단점)
      - [1.2.1.2. 절차지향 언어(c-like) 가 대형시스템 개발하기에 불편한 이유?](#1212-절차지향-언어c-like-가-대형시스템-개발하기에-불편한-이유)
    - [1.2.2. Encapsulation](#122-encapsulation)
    - [1.2.3. Information Hiding](#123-information-hiding)
    - [1.2.4. **Inheritance**](#124-inheritance)
    - [1.2.5. **Polymorphism**](#125-polymorphism)
      - [1.2.5.1. Dynamic Binding이 OOP에서 중요한 이유?](#1251-dynamic-binding이-oop에서-중요한-이유)
      - [1.2.5.2. OOP에서 동적 바인딩이 무엇인가?](#1252-oop에서-동적-바인딩이-무엇인가)
    - [1.2.6. Abstract Class, Interface](#126-abstract-class-interface)
    - [1.2.7. Generic Class/Template](#127-generic-classtemplate)
  - [1.3. OOAD](#13-ooad)
    - [1.3.1. Usecase Diagram](#131-usecase-diagram)
      - [1.3.1.1. 유스케이스 다이어그램의 구성요소는 무엇인가?](#1311-유스케이스-다이어그램의-구성요소는-무엇인가)
      - [1.3.1.2. 유즈케이스 다이어그램에서, 고정된 실행 순서에 대해 (1) actor가 단일 호출로 일괄 실행 vs (2)actor가 개별 호출로 개별 실행가 맞을까](#1312-유즈케이스-다이어그램에서-고정된-실행-순서에-대해-1-actor가-단일-호출로-일괄-실행-vs-2actor가-개별-호출로-개별-실행가-맞을까)
      - [1.3.1.3. usecase를 코드로 표현한다면 어떻게 구현이 되는가?](#1313-usecase를-코드로-표현한다면-어떻게-구현이-되는가)
      - [1.3.1.4. 유스케이스 다이어그램은 어디에 사용되는가?](#1314-유스케이스-다이어그램은-어디에-사용되는가)
    - [1.3.2. Class Diagram](#132-class-diagram)
      - [1.3.2.1. Class Diagram에서 Relationship 은 무엇인가?](#1321-class-diagram에서-relationship-은-무엇인가)
      - [1.3.2.2. (component) interface란 무엇인가?](#1322-component-interface란-무엇인가)
      - [1.3.2.3. class diagram에서 relationship은 어떤 의미인가 (A-B 사이에 줄을 긋는 의미)?](#1323-class-diagram에서-relationship은-어떤-의미인가-a-b-사이에-줄을-긋는-의미)
      - [1.3.2.4. A와 B 사이에 Association이 좋은지 Aggregation이 좋은지 판단해야할 때 어떤 기준으로 판단해야하는가?](#1324-a와-b-사이에-association이-좋은지-aggregation이-좋은지-판단해야할-때-어떤-기준으로-판단해야하는가)
    - [1.3.3. Sequence Diagram](#133-sequence-diagram)
      - [1.3.3.1. sequence diagram에서 interaction operator 몇 종류가 있고 무엇들인지](#1331-sequence-diagram에서-interaction-operator-몇-종류가-있고-무엇들인지)
    - [1.3.4. State Machine Diagram](#134-state-machine-diagram)
      - [1.3.4.1. state machine diagram은 어떤 경우에 활용하면 좋을까?](#1341-state-machine-diagram은-어떤-경우에-활용하면-좋을까)
    - [1.3.5. Timing Diagram](#135-timing-diagram)
    - [1.3.6. Activity Diagram](#136-activity-diagram)
    - [1.3.7. Component Diagram](#137-component-diagram)
      - [1.3.7.1. Component Diagram은 언제, 어떤 용도로 그릴까?](#1371-component-diagram은-언제-어떤-용도로-그릴까)
      - [1.3.7.2. 우리가 배운 UML 중에 white box 컴포넌트를 모델링한 다이어그램](#1372-우리가-배운-uml-중에-white-box-컴포넌트를-모델링한-다이어그램)
    - [1.3.8. Deployment Diagram](#138-deployment-diagram)
      - [1.3.8.1. Deployment Diagram은 어떤어떤 구성요소가 있을까?](#1381-deployment-diagram은-어떤어떤-구성요소가-있을까)
    - [1.3.9. UML Constructs for Parallel Processing](#139-uml-constructs-for-parallel-processing)
    - [1.3.10. Consistency](#1310-consistency)
  - [1.4. Design Patterns](#14-design-patterns)
    - [1.4.1. Principles of Design Patterns](#141-principles-of-design-patterns)
    - [1.4.2. Classification of Design Patterns](#142-classification-of-design-patterns)
    - [1.4.3. 각 패턴별](#143-각-패턴별)
      - [1.4.3.1. 전략 패턴은 언제 쓰는게 좋을까?](#1431-전략-패턴은-언제-쓰는게-좋을까)
      - [1.4.3.2. abstract factory 패턴은 언제 쓰는게 좋을까? 그리고 어떻게 작동하는가?](#1432-abstract-factory-패턴은-언제-쓰는게-좋을까-그리고-어떻게-작동하는가)
      - [1.4.3.3. 빌더 패턴은 언제, 어떤 용도로 사용할까?](#1433-빌더-패턴은-언제-어떤-용도로-사용할까)
      - [1.4.3.4. visitor 패턴을 쓰면 기대할 수 있는 장점?](#1434-visitor-패턴을-쓰면-기대할-수-있는-장점)
    - [1.4.4. Common OO 메커니즘](#144-common-oo-메커니즘)
    - [1.4.5. Advanced Topics](#145-advanced-topics)
  - [1.5. Requirement Engineering](#15-requirement-engineering)
    - [1.5.1. SW Quality의 정의](#151-sw-quality의-정의)
    - [1.5.2. Quality Aspects의 유형](#152-quality-aspects의-유형)
    - [1.5.3. Quality Model of ISO 9126](#153-quality-model-of-iso-9126)
      - [1.5.3.1. ISO 9126에서 말하고 있는 efficiency 란 어떤 것인가?](#1531-iso-9126에서-말하고-있는-efficiency-란-어떤-것인가)
      - [1.5.3.2. ISO 9126의 Maturity를 충족시키기 위한 tactic은 무엇인가?](#1532-iso-9126의-maturity를-충족시키기-위한-tactic은-무엇인가)
  - [1.6. Architecture Style](#16-architecture-style)
    - [1.6.1. Batch Sequential, Pipe-n-filter](#161-batch-sequential-pipe-n-filter)
    - [1.6.2. Layered, MVC](#162-layered-mvc)
    - [1.6.3. Blackboard, Shared Repository](#163-blackboard-shared-repository)
      - [1.6.3.1. Shared Repository 사용 용도는 무엇일까?](#1631-shared-repository-사용-용도는-무엇일까)
      - [1.6.3.2. Shared Repository 를 사용할 때 예상되는 단점?](#1632-shared-repository-를-사용할-때-예상되는-단점)
    - [1.6.4. Micro Kernel, Micro Service](#164-micro-kernel-micro-service)
    - [1.6.5. Dispatch, Broker](#165-dispatch-broker)
    - [1.6.6. Understanding Architecture Styles](#166-understanding-architecture-styles)
      - [1.6.6.1. 본인이 적용한 스타일이 왜 효율적(efficient) 한가?](#1661-본인이-적용한-스타일이-왜-효율적efficient-한가)
  - [1.7. Applying Viewpoints](#17-applying-viewpoints)
    - [1.7.1. Essential Viewpoints](#171-essential-viewpoints)
    - [1.7.2. Guidelines for each view](#172-guidelines-for-each-view)
  - [1.8. Applying Tactics for NFR](#18-applying-tactics-for-nfr)
    - [1.8.1. Architecture Design for Conventional NFRs](#181-architecture-design-for-conventional-nfrs)
      - [1.8.1.1. CEP에서 제안된 X tactic의 정당성을 보여주세요](#1811-cep에서-제안된-x-tactic의-정당성을-보여주세요)
      - [1.8.1.2. Redundancy 관련 택틱과 스타일 간의 차이점](#1812-redundancy-관련-택틱과-스타일-간의-차이점)
    - [1.8.2. Architecture Design for Non-Conventional NFRs](#182-architecture-design-for-non-conventional-nfrs)
      - [1.8.2.1. Architectural Concern과 Non-Function Requirements 간 관계 설명해보기](#1821-architectural-concern과-non-function-requirements-간-관계-설명해보기)
    - [1.8.3. Impact of Tactics on Views](#183-impact-of-tactics-on-views)
  - [1.9. Architectural Evaluation](#19-architectural-evaluation)
    - [1.9.1. ATAM](#191-atam)
  - [1.10. 기타](#110-기타)
    - [1.10.1. 디자인은 무엇인가?](#1101-디자인은-무엇인가)
    - [1.10.2. 디자인 패턴은 무엇인가?](#1102-디자인-패턴은-무엇인가)
    - [1.10.3. 패턴을 적용해 문제 해결한 경험? 업무에서 어떤때 패턴을 적용했는가?](#1103-패턴을-적용해-문제-해결한-경험-업무에서-어떤때-패턴을-적용했는가)
    - [1.10.4. SW 테스팅이란 무엇인가?](#1104-sw-테스팅이란-무엇인가)
    - [1.10.5. SW 품질이 무엇인가?](#1105-sw-품질이-무엇인가)
      - [1.10.5.1. 클라우드 서비스에서 로드밸런스 구조가 필요할 것인가?](#11051-클라우드-서비스에서-로드밸런스-구조가-필요할-것인가)
      - [1.10.5.2. 커플링과 디커플링 차이는?](#11052-커플링과-디커플링-차이는)
      - [1.10.5.3. Validation과 Verification의 차이?](#11053-validation과-verification의-차이)
      - [1.10.5.4. SW Review와 Test의 차이?](#11054-sw-review와-test의-차이)


# 1. 면접

## 1.1. 공통사항
### 1.1.1. 2분 자기 소개해보세요
안녕하세요, DataPlatform그룹 김건호입니다. 
저는 그룹 내 Datalake 솔루션 파트에 소속되어, 임직원 대상 Datalake 서비스에 대한 개발과 운영 업무를 수행하고 있습니다.  
과정을 수행하며 아키텍처에 대한 기초 활용 역량을 갖추게 되었다는 점

## 1.2. OOP Concepts

### 1.2.1. Object-Oriented Paradigm
- Compared to Procedural Programming
#### 1.2.1.1. 절차지향 언어의 단점?
#### 1.2.1.2. 절차지향 언어(c-like) 가 대형시스템 개발하기에 불편한 이유?
- 절차지향 언어는 커플링이 높음
  - 절차지향 언어이므로 시스템이 커질수록 모듈화라던지 확장성/재사용성(다형성, 상속 in OOP)이 떨어짐
  - 글로벌 베리어블 사용 -> 결합도 증가, 안전하지 않음
  - 모듈화 하기 힘듬 --> OOP는 캡슐화로 데이터와 메소드를 감출 수 있음
  - 이식성이 떨어짐: malloc 이 os specific 하므로 이식성이 떨어짐
### 1.2.2. Encapsulation

### 1.2.3. Information Hiding
- Visibility

### 1.2.4. **Inheritance**

### 1.2.5. **Polymorphism**
- Overloading
- Overriding
- Dynamic Binding
#### 1.2.5.1. Dynamic Binding이 OOP에서 중요한 이유?
  - it plays a critical role in enabling polymorphism and providing flexibility and extensibility to software systems
#### 1.2.5.2. OOP에서 동적 바인딩이 무엇인가?
- 슈퍼클래스가 정의한 메소드를 서브클래스가 상속받고, 런타임에 호출될 함수가 결정되는 것

- Substitutability

### 1.2.6. Abstract Class, Interface
- Abstract Class와 Interface의 차이점

### 1.2.7. Generic Class/Template

## 1.3. OOAD

### 1.3.1. Usecase Diagram
- Relationships, Granularity of Use Cases
- Use Case Description/Scenario
#### 1.3.1.1. 유스케이스 다이어그램의 구성요소는 무엇인가?
- 표준 구성요소
  - Actor
  - Usecase
  - Relation
    - Invoke (actor - usecase 간)
    - Inter usecase Rel (usecase 간)
      - General, Extend, Include
#### 1.3.1.2. 유즈케이스 다이어그램에서, 고정된 실행 순서에 대해 (1) actor가 단일 호출로 일괄 실행 vs (2)actor가 개별 호출로 개별 실행가 맞을까
- usecase diagram에서 실행순서를 나타낼 목적으로 include를 사용하는 경우는 오용이다.
- include는 포함관계를 나타낼 뿐, 순서를 표시하지 않음
- mediator object가 행위를 결정짓는것이 바람직함. 즉 (2)이 맞다
#### 1.3.1.3. usecase를 코드로 표현한다면 어떻게 구현이 되는가?
- 특정 클래스 안의 오퍼레이션으로 매핑
#### 1.3.1.4. 유스케이스 다이어그램은 어디에 사용되는가?

### 1.3.2. Class Diagram
- 5 types of Relationships을 순서를 매기고 정의하시오
#### 1.3.2.1. Class Diagram에서 Relationship 은 무엇인가?
- 인스턴스 간의 링크가 어떤지를 나타낸 것.
  - ERD에서 카디널리티로 관계를 나타내것과 유사
  - 카디널리티가 구현될 수 있도록 코딩한다.
#### 1.3.2.2. (component) interface란 무엇인가?
- 내부의 동작에 대해 알 필요 없이 invoke 하기 편하게 만든 메소드의 집합
#### 1.3.2.3. class diagram에서 relationship은 어떤 의미인가 (A-B 사이에 줄을 긋는 의미)?
- A-B가 '관계'가 있다는 의미
  - 1) (클래스가 아닌) 인스턴스 간의 '영구적인 의존도'(=링크) 를 남기겠다.
  - 2) (런타임에) interaction paths for message passing
#### 1.3.2.4. A와 B 사이에 Association이 좋은지 Aggregation이 좋은지 판단해야할 때 어떤 기준으로 판단해야하는가?
- association 은 동등관계 e.g. 학생-과목, 고객-계좌
- aggregation 은 부품 객체가 없으면 전체객체는 생성하면 안되는 경우를 의미
### 1.3.3. Sequence Diagram
- Workflow related to Use Case Description
- Applying MVC style paradigm in drawing Sequence Diagram
#### 1.3.3.1. sequence diagram에서 interaction operator 몇 종류가 있고 무엇들인지


### 1.3.4. State Machine Diagram
- Transition, Event, Guard, Action
- State Machine Diagram에서 Event는 무엇인가요? 예시도 들어주세요
#### 1.3.4.1. state machine diagram은 어떤 경우에 활용하면 좋을까?
- state sensitive 또는 state dependent 한 behavior를 가지고 있을 때 사용
  - e.g. 자동차의 모드 중 D에서 시동을 끄고 이후에 다시 시동을 걸려고 할 때
- (+a) State와 Transition 두가지로 구성된다. ...
### 1.3.5. Timing Diagram

### 1.3.6. Activity Diagram
- action, activity
- 언제 Activity Diagram을 사용합니까?

### 1.3.7. Component Diagram
- provided Interface, Required Interface
- Required interface가 중요한 이유?
- pluggable Object
####  1.3.7.1. Component Diagram은 언제, 어떤 용도로 그릴까?
#### 1.3.7.2. 우리가 배운 UML 중에 white box 컴포넌트를 모델링한 다이어그램
- Pacakge Diagram: 인터페이스가 없고 컴포넌트들만 모아둔 것 --> white box (e.g. Java 패키지들)
- Component Diagram: 인터페이스를 표현 --> black box
### 1.3.8. Deployment Diagram
- Node, Artifacts
#### 1.3.8.1. Deployment Diagram은 어떤어떤 구성요소가 있을까?
- 표준항목이 정해져있음
- 노드(디바이스, Execution/Environ)
- 네트워크 커넥티비티(노드 간)
- 소프트웨어 아티팩트(노드 내)
- 사각형 박스에 stereotype 써서 표현

### 1.3.9. UML Constructs for Parallel Processing
- Available in UML Diagrams

### 1.3.10. Consistency
- Among Use Case Model, Class Diagram & Sequence Diagram
- Between Statemachine Diagram & Class Diagram
- Between Activity Diagram & Use Case Diagram
- X 다이어그램과 Y 다이어그램 간 consistency check는 어떻게 하는가

## 1.4. Design Patterns

### 1.4.1. Principles of Design Patterns
- OCP
  - OCP의 이점
  - OCP 구현의 메커니즘은?
- ISP   
  - 
- LSP

### 1.4.2. Classification of Design Patterns
- 생성 패턴
- 구조 패턴
- 행위 패턴
- [image](./image/a.jpg)

### 1.4.3. 각 패턴별
- 상황
- 클래스다이어그램 구조
- 협력
- 장단점
#### 1.4.3.1. 전략 패턴은 언제 쓰는게 좋을까?
우리가 필요로 하는 어떤 기능이 있는데, 기능실행에 필요한 인터페이스(메소드)의 시그니처(what)는 고정되어있고, 내부적인 알고리즘(how)을 교체하고자 할 때 사용
#### 1.4.3.2. abstract factory 패턴은 언제 쓰는게 좋을까? 그리고 어떻게 작동하는가?
#### 1.4.3.3. 빌더 패턴은 언제, 어떤 용도로 사용할까?
- 가변적인 객체를 만들고, 절차가 고정되어 있을 때 사용한다.
#### 1.4.3.4. visitor 패턴을 쓰면 기대할 수 있는 장점?

### 1.4.4. Common OO 메커니즘
- Abstraction with Interface
- Inheritance / Specialization
- Dynamic Binding
- Delegation
- X 패턴에서 사용된 OO 메커니즘?

### 1.4.5. Advanced Topics
- 패턴간 유사성
- 패턴간 차이점

## 1.5. Requirement Engineering

### 1.5.1. SW Quality의 정의

### 1.5.2. Quality Aspects의 유형
- Process Quality
  - PQ가 중요한 이유
- Internal Quality
- External Quality
- Quality in Use
  - QU가 중요한 이유

### 1.5.3. Quality Model of ISO 9126
- 6 main factors and sub factors for each
- X 유형의 시스템 개발 시 중요한 Quality Factor는?
#### 1.5.3.1. ISO 9126에서 말하고 있는 efficiency 란 어떤 것인가?
#### 1.5.3.2. ISO 9126의 Maturity를 충족시키기 위한 tactic은 무엇인가?

## 1.6. Architecture Style

### 1.6.1. Batch Sequential, Pipe-n-filter

### 1.6.2. Layered, MVC

### 1.6.3. Blackboard, Shared Repository
#### 1.6.3.1. Shared Repository 사용 용도는 무엇일까?
- 2가지 조건이 있다
  - 데이터를 사용하는 클라이언트가 여러 종류이고 효율적으로 데이터를 공유할 때 사용
  - DB 스키마가 안정적일 때 사용

#### 1.6.3.2. Shared Repository 를 사용할 때 예상되는 단점?
- Repository의 Failure가 발생하면 모든 클라이언트에 영향
- 특정 데이터 스트럭처가 바뀌면 관련된 클라이언트가 바꿔야 함
  
### 1.6.4. Micro Kernel, Micro Service

### 1.6.5. Dispatch, Broker

### 1.6.6. Understanding Architecture Styles
- 상황
- 컴포넌트와 커넥터 구조
- 장단점
#### 1.6.6.1. 본인이 적용한 스타일이 왜 효율적(efficient) 한가?

## 1.7. Applying Viewpoints

### 1.7.1. Essential Viewpoints
- Functional
- Information
- Behavior
- Deployment view

### 1.7.2. Guidelines for each view
- X 뷰포인트 적용 절차는?
  
## 1.8. Applying Tactics for NFR

### 1.8.1. Architecture Design for Conventional NFRs
- Tactics for Common NFRs: Available
#### 1.8.1.1. CEP에서 제안된 X tactic의 정당성을 보여주세요

#### 1.8.1.2. Redundancy 관련 택틱과 스타일 간의 차이점
- 목적이 다르다
  - 스타일(dispatcher, broker) -> 시스템 전체 결정. 로드밸런싱으로 고성능
    - 로드밸런싱 하다보면 부분적으로 Mature 특성이 적용될 수 있음.
  - 택틱(Availability 중 Redundancy) -> 시스템 fail 안나는 목적
### 1.8.2. Architecture Design for Non-Conventional NFRs
- Tactics to be devised by Architectures
- 자율주행 SW 가 나온다고 하면 safety가 있습니다. 이를 효과적으로 높일 수 있는 택틱은 뭐가 있을까요?
  - 틀려도 괜찮음
#### 1.8.2.1. Architectural Concern과 Non-Function Requirements 간 관계 설명해보기

### 1.8.3. Impact of Tactics on Views


## 1.9. Architectural Evaluation

### 1.9.1. ATAM
- ATAM 적용 절차는?
- 그외 평가방법
  - 이번 과정의 교육 범위가 아닙니다로 답변

## 1.10. 기타
### 1.10.1. 디자인은 무엇인가?
- Design은 Implementation에 필요한 핵심적인 decision making이다..
- 디자인이 구현을 결정한다
- 구현에 도움이 되는 설계를 해야함
### 1.10.2. 디자인 패턴은 무엇인가?
- 디자인 패턴은 자주 나오는 문제에 대해 재사용 가능한 솔루션. 시스템의 부분부분 적용되는 스코프
- 아키텍처 스타일(패턴)은 시스템 전체에 적용되는 스코프
### 1.10.3. 패턴을 적용해 문제 해결한 경험? 업무에서 어떤때 패턴을 적용했는가?
### 1.10.4. SW 테스팅이란 무엇인가?
- 테스팅 (테스팅 목적)은 오류(defect, 결함)를 검출하는 것.
- 테스팅은 완벽하지 못함.(한계가 있음 - 테스팅 커버리지가 100%가 안되는 현실). 이래서 설계단계가 중요함. 디자인 리뷰 필수
### 1.10.5. SW 품질이 무엇인가?
- 기능적/비기능적 요구사항을 준수하는가
- 성능과 부하에 대한 기준을 충족하는가
- implicit, explicit 요구사항을 만족하는가
  - implicit: 유추할 수 있는 요구사항
    - 예상되는 가변성을 고려해서 설계
    - 즉 요구사항이 변경되도 수정가능하게 설계
#### 1.10.5.1. 클라우드 서비스에서 로드밸런스 구조가 필요할 것인가?
- 글로벌 사용자 요청의 부하분산
- 백엔드 서버 장애 시 고가용성
#### 1.10.5.2. 커플링과 디커플링 차이는?
- 커플링: A와 B가 서로 접근하거나 참조. B의 변경 사항이 A에 전파됨
  - 일반적으로 결합도가 낮을수록 좋다

#### 1.10.5.3. Validation과 Verification의 차이?
- Validation: 사용자 중심. 요구사항에 부합한지.
- Verification: 개발자 중심. 기술적으로 정확성에 대한 것.
#### 1.10.5.4. SW Review와 Test의 차이?
- 수행 대상의 차이가 있다.
  - Review: 디자인이나 소스코드 리뷰. 아웃풋이 안나옴 
  - Test: 시스템 운영. 아웃풋이 나온다
