
# 이 파일에 게임 스크립트를 입력합니다. (파이썬)

# image 문을 사용해 이미지를 정의합니다. idle 같은 경우에는 기본형이다.
# 캐릭터 CG 처음등장할 때와 사라질 때만 Dissolve 효과 넣고, 표정 변화할 때는 아니다.
# 장소는 Scene, 효과는 Fade로만 하기

##########################################################

#Riel 낮(b)
image Riel b idle = "cg/riel/b/Riel_idle.png"
image Riel b angry = "cg/riel/b/Riel_angry.png"
image Riel b smile = "cg/riel/b/Riel_smile.png"
image Riel b solid = "cg/riel/b/Riel_solid.png"
image Riel b surp = "cg/riel/b/Riel_surp.png"
image Riel b notfunny = "cg/riel/b/Riel_nf.png"
image Riel b shy = "cg/riel/b/Riel_shy.png"
image Riel b terra = "cg/riel/b/Riel_terra.png"


#Riel 밤(a)
image Riel a idle = "cg/riel/a/Riel_idle.png"
image Riel a angry = "cg/riel/a/Riel_angry.png"
image Riel a smile = "cg/riel/a/Riel_smile.png"
image Riel a solid = "cg/riel/a/Riel_solid.png"
image Riel a surp = "cg/riel/a/Riel_surp.png"
image Riel a notfunny = "cg/riel/a/Riel_nf.png"
image Riel a shy = "cg/riel/a/Riel_shy.png"
image Riel a terra = "cg/riel/a/Riel_terra.png"


#Lina 낮(b) only right
image Lina b idle = "cg/lina/b/Lina_idle.png"
image Lina b angry = "cg/lina/b/Lina_angry.png"
image Lina b smile = "cg/lina/b/Lina_smile.png"
image Lina b surp = "cg/lina/b/Lina_surp.png"
image Lina b shy = "cg/lina/b/Lina_shy.png"
image Lina b solid = "cg/lina/b/Lina_solid.png"
image Lina b worry = "cg/lina/b/Lina_worry.png"
image Lina b notfunny = "cg/lina/b/Lina_nf.png"

#Lina 밤(a) only right
image Lina a idle = "cg/lina/a/Lina_idle.png"
image Lina a angry = "cg/lina/a/Lina_angry.png"
image Lina a smile = "cg/lina/a/Lina_smile.png"
image Lina a surp = "cg/lina/a/Lina_surp.png"
image Lina a shy = "cg/lina/a/Lina_shy.png"
image Lina a solid = "cg/lina/a/Lina_solid.png"
image Lina a worry = "cg/lina/a/Lina_worry.png"
image Lina a notfunny = "cg/lina/a/Lina_nf.png"

#Oscar 낮(b) only at left
image Oscar b idle = "cg/oscar/b/Oscar_idle.png"
image Oscar b angry = "cg/oscar/b/Oscar_angry.png"
image Oscar b smile = "cg/oscar/b/Oscar_smile.png"
image Oscar b solid = "cg/oscar/b/Oscar_solid.png"
image Oscar b surp = "cg/oscar/b/Oscar_surp.png"
image Oscar b shy = "cg/oscar/b/Oscar_shy.png"
image Oscar b envy = "cg/oscar/b/Oscar_envy.png"
image Oscar b mental = "cg/oscar/b/Oscar_mb.png"

#Oscar 밤(a) only at left
image Oscar a idle = "cg/oscar/a/Oscar_idle.png"
image Oscar a angry = "cg/oscar/a/Oscar_angry.png"
image Oscar a smile = "cg/oscar/a/Oscar_smile.png"
image Oscar a solid = "cg/oscar/a/Oscar_solid.png"
image Oscar a surp = "cg/oscar/a/Oscar_surp.png"
image Oscar a shy = "cg/oscar/a/Oscar_shy.png"
image Oscar a envy = "cg/oscar/a/Oscar_envy.png"
image Oscar a mental = "cg/oscar/a/Oscar_mb.png"

#Teacher 낮(b)
image Teacher b idle = "cg/teacher/b/Teacher_idle.png"
image Teacher b angry = "cg/teacher/b/Teacher_angry.png"
image Teacher b smile = "cg/teacher/b/Teacher_smile.png"
image Teacher b solid = "cg/teacher/b/Teacher_solid.png"
image Teacher b notfunny = "cg/teacher/b/Teacher_nf.png"
image Teacher b surp = "cg/teacher/b/Teacher_surp.png"

#Teacher 밤(a)
image Teacher a idle = "cg/teacher/a/Teacher_idle.png"
image Teacher a angry = "cg/teacher/a/Teacher_angry.png"
image Teacher a smile = "cg/teacher/a/Teacher_smile.png"
image Teacher a solid = "cg/teacher/a/Teacher_solid.png"
image Teacher a notfunny = "cg/teacher/a/Teacher_nf.png"
image Teacher a surp = "cg/teacher/a/Teacher_surp.png"


#principal 낮(b)
image Principal b idle = "cg/principal/b/Principal_idle.png"
image Principal b angry = "cg/principal/b/Principal_angry.png"
image Principal b smile = "cg/principal/b/Principal_smile.png"
image Principal b solid = "cg/principal/b/Principal_solid.png"

#principal 밤(a)
image Principal a idle = "cg/principal/a/Principal_idle.png"
image Principal a angry = "cg/principal/a/Principal_angry.png"
image Principal a smile = "cg/principal/a/Principal_smile.png"
image Principal a solid = "cg/principal/a/Principal_solid.png"


#Trey 낮(b) only at right
image Trey b idle = "cg/trey/b/Trey_idle.png"
image Trey b smile = "cg/trey/b/Trey_smile.png"
image Trey b solid = "cg/trey/b/Trey_solid.png"
image Trey b abb = "cg/trey/b/Trey_abb.png"
image Trey b surp = "cg/trey/b/Trey_surp.png"
image Trey b shy = "cg/trey/b/Trey_shy.png"

#Trey 밤(a) only at right
image Trey a idle = "cg/trey/a/Trey_idle.png"
image Trey a smile = "cg/trey/a/Trey_smile.png"
image Trey a solid = "cg/trey/a/Trey_solid.png"
image Trey a abb = "cg/trey/a/Trey_abb.png"
image Trey a surp = "cg/trey/a/Trey_surp.png"
image Trey a shy = "cg/trey/a/Trey_shy.png"



#jane 낮(b)
image Jane b idle = "cg/jane/b/Jane_idle.png"
image Jane b smile = "cg/jane/b/Jane_smile.png"
image Jane b angry = "cg/jane/b/Jane_angry.png"
image Jane b sad = "cg/jane/b/Jane_sad.png"
image Jane b shy = "cg/jane/b/Jane_shy.png"
image Jane b shy2 = "cg/jane/b/Jane_shy2.png"
image Jane b solid = "cg/jane/b/Jane_solid.png"
image Jane b surp = "cg/jane/b/Jane_surp.png"


#jane 밤(a)
image Jane a idle = "cg/jane/a/Jane_idle.png"
image Jane a smile = "cg/jane/a/Jane_smile.png"
image Jane a angry = "cg/jane/a/Jane_angry.png"
image Jane a sad = "cg/jane/a/Jane_sad.png"
image Jane a shy = "cg/jane/a/Jane_shy.png"
image Jane a shy2 = "cg/jane/a/Jane_shy2.png"
image Jane a solid = "cg/jane/a/Jane_solid.png"
image Jane a surp = "cg/jane/a/Jane_surp.png"


#Student 1 낮(b)
image Student1 b idle = "cg/student1/b/Student1_idle.png"
image Student1 b angry = "cg/student1/b/Student1_angry.png"
image Student1 b pet = "cg/student1/b/Student1_pet.png"


#Student 1 밤(a)
image Student1 a idle = "cg/student1/a/Student1_idle.png"
image Student1 a angry = "cg/student1/a/Student1_angry.png"
image Student1 a pet = "cg/student1/a/Student1_pet.png"


#Student 2 낮(b) only right
image Student2 b idle = "cg/student2/b/Student2_idle.png"
image Student2 b angry = "cg/student2/b/Student2_angry.png"
image Student2 b pet = "cg/student2/b/Student2_pet.png"


#Student 2 밤(a) only right
image Student2 a idle = "cg/student2/a/Student2_idle.png"
image Student2 a angry = "cg/student2/a/Student2_angry.png"
image Student2 a pet = "cg/student2/a/Student2_pet.png"


##################################################################

#Scene 장소
image pl1 = "pl/1.jpg"
image pl2 = "pl/2.jpg"
image pl3 = "pl/3.jpg"
image pl4 = "pl/4.png"
image pl5 = "pl/5.jpg"
image pl6 = "pl/6.jpg"
image pl7 = "pl/7.jpg"
image pl8 = "pl/8.jpg"
image pl9 = "pl/9.jpg"
image pl10 = "pl/10.jpg"
image pl11 = "pl/11.jpg"
image pl12 = "pl/12.jpg"
image pl13 = "pl/13.jpg"
image pl14 = "pl/14.jpg"
image pl15 = "pl/15.jpg"
image pl16 = "pl/16.png"
image pl17 = "pl/17.jpg"
image pl18 = "pl/18.jpg"
image pl19 = "pl/19.png"
image pl20 = "pl/20.jpg"
image pl21 = "pl/21.png"
image pl22 = "pl/22.jpg"
image pl23 = "pl/23.png"
image pl24 = "pl/24.png"
image pl25 = "pl/25.jpg"
image pl26 = "pl/26.jpg"
image pl27 = "pl/27.png"
image pl28 = "pl/28.png"
image pl29 = "pl/29.jpg"
image pl30 = "pl/30.png"
image pl31 = "pl/31.jpg"
image pl32 = "pl/32.png"
image pl33 = "pl/33.png"
image pl34 = "pl/34.png"
image pl35 = "pl/35.png"
image pl36 = "pl/36.png"
image pl37 = "pl/37.png"
image pl38 = "pl/38.png"
image pl39 = "pl/39.jpg"
image pl40 = "pl/40.jpg"


##################################################################
#일러스트
image il1 = "il/1.png"
image il2 = "il/2.png"
image il3 = "il/3.png"
image il4 = "il/4.png"
image il5 = "il/5.png"
image il6 = "il/6.png"
image il7 = "il/7.png"
image il75 = "il/7.5.jpg"
image il8 = "il/8.png"
image il9 = "il/9.png"
image il10 = "il/10.png"
image il11 = "il/11.png"
image il12 = "il/12.png"
image il122 = "il/12-2.png"
image il13 = "il/13.png"
image il14 = "il/14.png"
image il15 = "il/15.png"
image il16 = "il/16.png"
image il17 = "il/17.png"
image il18 = "il/18.png"
image il19 = "il/19.png"
image il20 = "il/20.png"
image il21 = "il/21.png"
image il22 = "il/22.png"
image il23 = "il/23.png"
image il24 = "il/24.png"
image il25 = "il/25.png"
image il26 = "il/26.png"
image il27 = "il/27.png"
image il28 = "il/28.png"
image il29 = "il/29.png"
image il30 = "il/30.png"
image il31 = "il/31.png"
image il32 = "il/32.png"
image il33 = "il/33.png"
image il34 = "il/34.jpg"
image il35 = "il/35.png"
image il36 = "il/36.png"
image il37 = "il/37.png"
image il38 = "il/38.png"
image il39 = "il/39.png"
image il40 = "il/40.png"
image il41 = "il/41.png"
image il42 = "il/42.png"
image il43 = "il/43.png"
image il44 = "il/44.png"
image il45 = "il/45.png"
image il46 = "il/46.png"
image il47 = "il/47.png"
image il48 = "il/48.png"
image il49 = "il/49.png"
image il50 = "il/50.png"
image il51 = "il/51.png"
image il52 = "il/52.png"
image il53 = "il/53.png"
image il54 = "il/54.png"
image il55 = "il/55.png"
image il56 = "il/56.png"
image a = "il/a.png"
image b = "il/b.png"
##################################################################
# 게임에서 사용할 캐릭터를 정의합니다.
define ch_News = Character("News", color="#937b73")
define ch_Riel = Character("Riel")
define ch_Lina = Character("Lina")
define ch_Oscar = Character("Oscar", color="#9966ff")
define ch_Teacher = Character("Teacher")
define ch_Principal = Character("Principal", color="#937b73")
define ch_Student1 = Character("Student 1")
define ch_Student2 = Character("Student 2")
define ch_Bully1 = Character("Bully 1", color="#937b73")
define ch_Bully2 = Character("Bully 2", color="#937b73")
define ch_unknown = Character("???", color="#000000")
define ch_Trey = Character("Trey")
define ch_Classmates = Character("Classmates")
define ch_Audio = Character("Audio", color="#937b73")
define ch_Jane = Character("Jane", color="#c34c4c")
define ch_Eyeless = Character("Eyeless girl", color="#ff0033")
define ch_Haberler = Character("Haberler", color="#937b73")
define ch_Ogretmen = Character("Öğretmen")
define ch_Mudur = Character("Mudur", color="#937b73")
define ch_Ogrenci1 = Character("Öğrenci 1")
define ch_Ogrenci2 = Character("Öğrenci 2")
define ch_Sinif = Character("Sınıf")
define ch_Radyo = Character("Radyo", color="#937b73")
define ch_Gozsuzkiz = Character("Gözleri Olmayan Kız", color="#ff0033")
define ch_Zorba1 = Character("Bully 1", color="#937b73")
define ch_Zorba2 = Character("Bully 2", color="#937b73")
init python:
 achievement.Sync()






##################################################################

# 여기에서부터 게임이 시작합니다.
label start:

 #music은 한 노래가 무한반복(배경음) sound는 1번만하고 멈춤(효과음)
 #play music "music.ogg"
 play music "bgm/1.mp3"

 #S#1. INT. 리엘의 집 / 오전

 #(뉴스화면 배경)
 show il1 with fade

 #계속해서 한 반에서 벌어지는 의문의 연쇄살인 기억하십니까? 안타깝게도 또 한 명의 희생자가 나왔습니다. 이 학생은 XX그룹회장의 아들로 더 큰 관심을 모으고 있는 데요. 이제 칼리고등학교의 2학년 3반은 한 학생밖에 남지 않게 되었…….
 ch_News "Do you remember the serial murder case that continues to happen within a certain class? Unfortunately, another victim has emerged"
 ch_News "This issue received even more attention, as the victim was the only son of XX group president. Now the third class of juniors in KALI High School's is left with only one student..."

 #(뉴스화면배경이 꺼지고 리엘이 등장한다) 더 이상 듣고 싶지 않아, 전원을 꺼버렸다.
 scene pl1 with fade
 show Riel b idle at center with dissolve
 "I didn't want to hear it anymore, so I turned it off. "

 show Riel b solid at center
 #리엘 : 우리 반 아이들은 의문의 살인자로 인해 한 명씩 죽어갔고, 결국 나밖에 남지 않았다.
 ch_Riel "Our classmates have been killed one by one by an unknown killer, and I am the only one who is left"

 #...그래도 학교는 가야겠지...
 "I still have to go to school…"

 show Riel b idle at center
 #우리 반엔 아무도 없지만...
 "even if no one is left..."

 hide Riel with dissolve

 #(배경에는 리엘의 부모님 사진이 나온다)
 show il2 with fade

 #우리 아빠. 엄마의 말에 따르면 불의의 사고에 돌아가셨다고 한다. 그리고 엄마는...
 "My father. according to mom, he died in an unfortunate accident. soon after, my mom…"

 #리엘 : (애써 밝게) 그만 생각해야지. 학교나 가자! 학교 다녀오겠습니다. ...엄마, 아빠.
 ch_Riel "Whatever. let's stop thinking about it and go to school! ...See you later. mom, and dad."

 #S#2. INT. 교장실 앞 / 오전
 scene pl2 with fade

 show Riel b solid at center with dissolve

 #리엘 : (어두운 표정으로) 교장선생님이 범인으로 날 의심하다니… 게다가 케이까지 내가 죽였다고? 케이는 어릴 적부터 나와 소꿉친구였는데, 내가 왜 케이를!!
 ch_Riel "The principal thinks that I am the murderer... Not to mention that he thinks I killed Kai.. He was my childhood friend, I would never kill him!!"

 show Riel b idle at center

 ch_Riel "He was my childhood friend, I would never kill him!!"

 $ achievement.grant("Murderer")
 $ achievement.Sync()


 hide Riel with dissolve

 #S#3. INT. 복도 / 정오
 show il3 with fade
 #(리엘이 복도를 지나가고 있다.  복도에는 아이들로 가득하다.)

 #쉬는 시간. 복도를 지나가는 아이들은 나를 힐끔힐끔 쳐다보고 있다. 저 아이들도 날 의심하는 걸까?
 "It's break time. The students in the hallway are giving me the looks. Could they be suspecting me too?"


 #학생1 : 쟤가 쟤네 반 애들 다 죽였다며?
 ch_Student1 "Hey, isn't that the guy who killed all of his classmates?"
 #학생2 : 뻔뻔하게 학교 나오는 것 좀 봐. 무서워 죽겠네.
 ch_Student2 "...and he has the nerve to show up to school? Scary stuff really"
 #모두들 나를 보며 수군거린다. 애써 안 들리는 척 해봤지만, 나도 모르게 고개가 숙여졌다.
 "Everyone's whispering to each other while staring at me. I pretended that I didn't hear anything, but I couldn't help lowering my head."
 #(리나 등장)

 scene pl3 with fade

 show Riel b idle at left with dissolve
 #리엘 : 아....
 ch_Riel "Ah ...."

 show Lina b worry at right with dissolve


 #리나 : (조심스럽게) 리엘... 괜찮아..?
 ch_Lina "Riel... you okay..?"

 show Lina b solid at right

 #리엘 : 응...
 ch_Riel "Yeah... "

 show Riel b solid at left

 #리나 : 저것들이 하는 말들 다 듣지 마. 널 하나도 모르는 애들이 마음대로 하는 소리야!
 ch_Lina "Don’t listen to them. They are just saying stupid stuffs without knowing anything about you!"

 show Lina b worry at right

 #리엘 : 넌 날 믿어주는 구나.
 ch_Riel "At least you trust me."

 show Riel b smile at left

 #리나 : 난 네가 그럴 애가 아니라는 걸 잘 아니깐!
 ch_Lina "Of course, I know you are not that kind of person!"

 #날 믿어주는 사람은 리나밖에 없었다. 리나는 어릴 적부터 나와 친구다. 아직까진.
 "Lina is the only one who believes me.Lina has been my friend since childhood. So far."

 hide Lina with dissolve

 show Riel b solid at left

 #불량스러운 생김새의 무리가 나에게 다가왔다.
 "Suddenly, a group of bullies came to me."

 show Student1 b idle at right with dissolve

 #일진1 : 얘가 그 유명한 살인자지?
 ch_Bully1 "He's the famous murderer, right?"

 show Riel b angry at left
 hide Student1 with dissolve

 show Student2 b idle at right with dissolve

 #일진2 : 살인자새끼가 철판이 두껍네. 너네 엄마가 그렇게 가르쳤냐?
 ch_Bully2 "You've got some nerve to show up like that, you murderer! Did your mother teach you to be like that? "


 #리엘 : (굳은 얼굴로) 엄마에 대해 함부로 말하지마.
 ch_Riel "Don’t you dare say bad things about my mother."

 show Riel b solid at left

 show Student2 b pet at right

 #일진2 : 아 맞다, 이 새끼 엄마 없다고 했었지.
 ch_Bully2 "Oh right, this bastard has no mother."

 #리엘 : ...
 ch_Riel "..."

 show Riel b idle at left

 hide Student2 with dissolve

 show Student1 b pet at right with dissolve

 #일진1 : 표정 봐라. 우리도 죽이겠다?
 ch_Bully1 "Would you look at his face. At this rate, he'll kill us all. Am I right?"

 hide Riel with dissolve
 hide Student1 with dissolve

 show Student1 b idle at left with dissolve
 show Lina b solid at right with dissolve

 #리나 : 너네...하지마...!
 ch_Lina "Guys.. stop it…!"

 show Student1 b pet at left

 #일진3 : 뭐야. 이 년은. 너 깔 이냐? (리나에게) 야.
 ch_Bully1 "Who's this bitch? Is she one your hoes?"

 show Student1 b angry at left

 ch_Bully1 "Hey."

 show Lina b angry at right

 #리나 : (화가 난 표정으로) ...
 ch_Lina "..."

 show Student1 b idle at left

 #일진3 : 너 조심해라. 저 살인자새끼 수틀리면 너한테도 칼 꼽을 테니깐.
 ch_Bully1 "You guys better be careful. He might stab you "

 hide Student1 with dissolve

 show Riel b terra at left with dissolve

 #리엘 : ....!!!
 ch_Riel "....!!!"

 #자기들끼리 키득거리는 소리에 리나의 얼굴은 붉어진다.
 "Lina was flushed with anger as they were chuckling."

 show Lina b shy at right

 #손에 힘이 가해지고, 주먹을 들 찰나에 한 손에 책을 든 귀찮은 표정의 아이가 우리 앞에 섰다.
 "Riel clenched his fists. Suddenly, a boy who was holding a book with an annoyed face appeared before us. "

 hide Riel with dissolve
 hide Lina with dissolve


 show Oscar b angry at left with dissolve

 #오스카 : (귀찮다는 표정으로) 아, 시끄럽네.
 ch_Oscar "You guys are so noisy."

 show Student2 b idle at right with dissolve

 #일진2 : 뭐야 이 범 생이 같은 놈은. 왜 조용히 해달라고 징징대러 왔다 보지.
 ch_Bully2 "If you know that, can you please shut up?"

 show Oscar b idle at left

 #오스카 : 알면 좀 조용히 하지.
 ch_Oscar "If you have already noticed, be quiet."

 show Student2 b angry at right

 #일진2 : 뭐?!
 ch_Bully2 "What?!"

 show Oscar b angry at left

 #오스카 : 여기가 너네만 쓰는 복도 아니니깐, 조용히 하라고.
 ch_Oscar "You don't own the hallway, so shut up."

 show Student2 b pet at right

 #일진2 : (화난 얼굴로)　이 범 생이 새끼가!
 ch_Bully2 "You nerd!"

 show Oscar b solid at left

 #오스카 : 무식한 게 자랑인가.
 ch_Oscar "Being stupid ain't something to be proud of."

 hide Oscar with dissolve
 hide Student2 with dissolve

 #(S) 종치는 소리
 play sound "sfx/1.mp3"

 show Student1 b pet at left with dissolve

 #일진1 : (일진2에게) 야, 그만해. 쟤 전교1등 오스카야. 쟤 건들면 피곤해지니깐, 종 쳤으니 이만 들어가자.
 ch_Bully1 "Cut it out. He is Oscar, the teacher's pet. Messing with him might cause some trouble, let's head back."

 show Student2 b pet at right with dissolve


 #일진2 : 쳇.
 ch_Bully2 "Tsk."

 hide Student1 with dissolve
 hide Student2 with dissolve

 show Oscar b idle at left

 #전교1등 오스카다. 오스카의 몇 마디에 불량배들은 찍소리도 못하고 반으로 들어갔다.
 "Scared of Oscar, the bullies became quiet and went back to their classroom."

 #아, 저 아이가 우릴 구해준 건가.
 "Ah, that boy saved us."

 #좋은 아이인 것 같다.
 "he must be a good guy."

 show Lina b smile at right with dissolve

 #리나 : (오스카에게) 고마워..
 ch_Lina "Thanks..."

 show Oscar b solid at left

 #오스카 : 뭐가?
 ch_Oscar "Thanks for what?"

 show Lina b idle at right

 #리나 : 우리 구해줘서.
 ch_Lina "...for saving us."

 show Oscar b idle at left

 #오스카 : 내가? 너넬?
 ch_Oscar "Me? save you guys?"

 show Lina b solid at right

 #리나 : 응?
 ch_Lina "huh?"

 show Oscar b angry at left

 #오스카 : 말 그대로 복도가 시끄러워서 나온 것뿐이야. 너네도 시끄럽게 하지 말고 비켜.
 ch_Oscar "Honestly, I came out here only because the hallway was too noisy. You guys too, stop being noisy and get out of my way..."

 hide Oscar with dissolve

 #오스카는 쌀쌀맞게 우리를 스쳐 지나갔다.
 "Oscar walked away coldly from us."

 #... 좋은 아이가 아니었군. 재수 없는 녀석이다.
 "...He isn’t as nice as I thought. Kind of annoying to be honest. "

 show Lina b idle at right

 #리나 : (어색하게) 하하..
 ch_Lina "Haha…"

 show Riel b idle at left with dissolve

 #리엘 : 뭐야, 저 녀석은. 리나 괜찮아?
 ch_Riel "What’s wrong with him? Are you okay, Lina?"

 #리나 : (리엘 에게) 난 괜찮아. ...나도 이제 그만 수업 들어 가봐야겠다. 리엘도 얼른 들어 가! 애들 하는 말은 신경 쓰지 말구! (밝게 웃으며) 파이팅!
 ch_Lina "I’m fine. I should go back to class. You should go back to class also!"
 ch_Lina "Forget about what everyone says!"

 show Lina b smile at right

 ch_Lina "Chin up!"

 show Riel b smile at left

 #리엘 : (웃으며) 그래, 리나 너도 수업 열심히 들어.
 ch_Riel "Okay, Lina. Have fun in class."

 hide Riel with dissolve
 hide Lina with dissolve

 show Riel b idle at center with dissolve

 #리나까지 교실로 들어가자, 복도에는 오직 나만이 남아있다.
 "Lina leaves, and I am left alone in the hallway."

 #(리엘의 표정이 급격히 굳는다.) (복도배경이 조금 어두워진다.)

 show Riel b solid at center

 #리엘 : 하루 사이에 많은 것이 바뀌었다. 나랑 친한 친구이었던 케이가 죽고..그 범인이 나로 몰리다니...! 아이들의 수군거리는 소리가 나를 숨 막히게 한다. 결국 난 리나와의 약속을 어 겨버린 채, 학교를 나와 버렸다. ..... 하지만 앞으로 어떻게 될 줄 알았더라면, 학교를 나오지 않았을 것이다... (완전히 암전)
 ch_Riel "A lot has changed in a day. Kai, who was a close friend of mine, died, and people think I killed him...! "

 show Riel b idle at center

 ch_Riel "It's hard to even breathe when I hear what they say about me. I broke the promise that I made with Lina and left the school."

 show Riel b solid at center

 ch_Riel "...But... If I knew what was awaiting for me, I would not have left the school..."

 hide Riel with dissolve

 stop music

 #S#4. EXT. 사원 / 오후
 scene pl4 with fade
 play music "bgm/2.mp3"

 #학교를 나와, 사원에 도착했다.
 "I left the school and arrived at the temple."

 #리엘 : 엄마와 자주 왔던 사원... 내가 답답하거나 힘든 일이 있을 테면 엄마와 종종 찾고 했 지만...엄마가 돌아가신 이후로는 처음이다. 혼자 온 사원은 왠지 모르게 낯설다.
 ch_Riel "This is the temple that I used to come often with my mother. I visited here often when I got sick or something bad happened to me."
 ch_Riel "But it is my first visit since my mother’s passing. It feels quite awkward to come here on my own."

 #INT. 사원 내부
 show il4 with fade

 #사원의 분위기는 웅장하면서도 묘하다. 마치 누군가가 쳐다보고 있는 것 같다. 난 방석 위에 무릎을 꿇고 눈을 감았다.
 "The temple had a both heavy and bizarre atmosphere. It even feels like someone is watching. I kneeled over the cushion and closed my eyes."

 show il5 with fade
 #리엘 : 억울함이 모두 사라지고... 모든 일들이 다 제자리를 찾기를...
 ch_Riel "I wish... I can prove my innocence and everything falls back into place."

 #...
 "..."

 #(잠시 화면이 어두워졌다가, 원래 배경으로 돌아온다. 배경에는 아까보다 붉은 기가 돈다.)

 #눈 감기 전 사원이 뭔가 달라진 것 같다. 붉은 기가 도는 것 같은데... 기분 탓이겠지. 텅 빈 사원 내부는 어떻게 보면 무서워 보이기도 하다.
 "I feel like something's changed I am probably just imagining it, but the Temple looks more red than before. The emptiness of the temple gave me the creeps."

 #리엘 : 이제 집에 가자.
 ch_Riel "Guess I'll go back home."

 show il6 with fade

 stop music

 #(리엘은 사원의 문을 연다.)

 #S#5. EXT. 길 가 / 밤
 scene pl5 with fade

 play music "bgm/3.mp3"

 #밖은 갑자기 비가 내리고 있다. 분명 아까는 맑았던 것 같은데, 지금은 안개가 가득 찬 것처럼 어둡고 뿌옇다. 잠깐. 지금... 몇 시지?
 "It is pouring outside. Pretty sure it was sunny just then, but now it's all foggy and dark. Wait. what time is it now?"

 #(리엘의 자신의 손목시계를 바라본다. 시계는 오후 2시를 가리키고 있다.)
 show il7 with fade

 #리엘 : (의문에 찬 표정으로) 아직 두시인데...
 ch_Riel "It's still only 2 PM."

 show il75 with fade
 #정류장을 향해 꽤 많이 걸었지만, 아무도 보이지 않는다. 수많은 가게들도 다 문이 닫혀있다.
 "Although it's been a while since I started walking towards the bus station, no one's in the street. The stores are all closed too."

 show il8 with fade
 #완전히 다른 세계로 온 것 같은 기분이 들기도 한다. 우선 정류장에서 버스를 기다리고 했다.
 "It felt like I came to a completely different world. I decided to just wait for the bus at the stop."

 #리엘 : 아, 버스다! 버스다.
 ch_Riel "Ah, finally.  The bus is here."

 show il9 with fade
 #(버스배경, 비어 있는 운전석) 근데... 버스기사가 없다...
 ch_Riel "The bus. But, wait, I don't see the driver..."

 #리엘 : 아무도 없어...? 대체 어떻게....
 ch_Riel "no one is driving it...? How could that happen..."

 #나는 뒷걸음질 쳐, 버스에서 내렸다.
 "I moved backwards, and quickly got off from the bus."

 #아무도 없는 버스는 다시 아무것도 보이지 않는 빈 공간을 향해 달려갔다. 갑자기 몸을 덮은 오한에 나는 비를 맞은 채 집으로 뛰어갔다.
 "The bus with no one inside disappeared into an empty space. I suddenly felt the cold, so I ran home through the rain."

 #S#6. INT. 리엘의 집 / 밤
 scene pl6 with fade

 #(S) 전화벨 소리
 play sound "sfx/2.mp3"

 #집으로 들어서자마자, 벨소리가 나를 반기고 있다. 내가 지금 집에 도착한 걸 누가 보고 있는 걸까.
 "As soon as I got home, the phone rang. It almost felt like somebody knew that I just arrived."

 #왠지 벨소리가 불길하다.
 "the ringtone feels ominous."

 show il10 with fade

 #나는 불안감을 애써 누르고, 전화를 받았다. 전화에서는 기계음이 섞인 목소리가 흘러나온다.
 "I tried to calm down and answered the phone call. On the telephone, I could hear a robotic voice."

 #전화 속 의문의 목소리 : 여기는 2학년 5반. 지금 당장 오지 않는다면, 네 여자친구인 리나는 평생 잊을 수 없는 끔찍함을 맛보게 될 거다.
 ch_unknown "I'm in the fifth classroom for juniors. If you don't come right now, your girlfriend Lina will taste the horror that she will never forget."

 #(S) 전화가 끊기는 소리
 play sound "sfx/3.mp3"
 #리엘 : (놀란 표정으로) 리나...? 리나..!!
 ch_Riel "Lina...? Lina!"

 #(암전)
 scene black with fade

 #나는 전화가 끊김과 동시에 학교로 뛰어갔다. 리나에게 무슨 일이 생길까봐 불안하다. 제발 아무 일도 없기를...
 "I rushed to the school, as soon as I hung off the phone. I was worried that something might happen to her. Please be safe... "

 #S#7. EXT. 학교 앞 / 밤
 scene pl7 with fade

 #리엘 : (힘든 표정으로) 하...하...
 ch_Riel "Ha...Ha..."

 #누군지 모르겠지만, 리나를 위협하고 있다.
 "I don't know who it is, but Lina is in danger."

 #대체 누가 나를 협박하는 것일까... 우선은 얼른 교실로 가서 리나를 구해야...!!
 "I wanna find out just who is threatening me. First of all, I need to go to the classroom to save her...!!"

 #(검정색 손이 다가와, 리엘의 입을 막는다. 리엘의 눈은 커진다.)
 show il11 with fade

 #리엘 : 읍..!
 ch_Riel "Urggh ..!"

 #(화면은 점차 어두워진다.)

 stop music

 #S#8. INT. 리엘의 교실 / 밤

 #(화면은 어두워졌다가, 원을 중심을 몇 번 깜빡 거리다가 점점 밝아진다.)

 play music "bgm/4.mp3"

 show il12 with fade

 #리엘 : (미간을 찌푸리고, 눈을 한쪽만 뜨며) 으...여긴?!
 ch_Riel "Arggghh...where am I?"

 show il122 with fade

 #교탁 앞엔 담임 선생님이 서있고, 반장인 트레이는 그 옆에 있다.
 "My homeroom teacher is standing in front of his desk, and Trey, the class president, is standing next to him."

 #자리는 우리 반 학생들로 가득 차 있다. 학생들이 불안한 표정으로 웅성거리자, 담임 선생님이 출석부로 교탁들 두 번 내리쳤다.
 "The seats are filled with class students. Students seemed to be worried and started whispering to each other. The teacher slammed the desk twice with the attendance book."

 #리엘 : 우리 반 교실...? 그리고 반장...케이까지... 분명 다 죽었는데, 어떻게...!
 ch_Riel "Our classroom...? and the class president...even Kei.. they were obviously all dead, but how...!"

 #담임 선생님 : 자 자 조용. 다들 진정해라. 내 말만 잘 들으면, 모두 무사할 수 있어!
 ch_Teacher "Ok guys, calm down. If you all follow my instruction, everyone will be safe"

 #트레이 : 그래, 애들아. 조용히 하고 선생님 말씀을 듣자.
 ch_Trey "Yeah, guys. Let's all settle down and listen to what he has to say."

 #담임 선생님 : 지금 학교에는 메두사 한 마리가 돌아다니고 있단다. 어디서 생겨났는지는 모르겠지만... 아무튼! 메두사를 만났을 시에는 덤벼볼 생각을 하지 말고 무조건 도망쳐야 한단 다. 메두사와 눈이 마주치면 심장박동수가 폭발적으로 올라가면서.... 결국 터지게 된다고 하니깐. 만약 위험한 일이 생긴다면 무조건 나에게로 오렴. 늘 교무실에 있을 테니. 내가 없을 때에는 반장이 나 대신이니 반장 말도 잘 듣고! 담임 선생님은 교실을 빠져나가려다가 멈춰 섰다.
 ch_Teacher "Now, a 'Medusa' is roaming around the school. I don't know where it came from...Anyways! When you encounter her, you should run away, and don't you dare fight against it. "
 ch_Teacher "If you make an eye contact with it, your heart rate will rise drastically.. Eventually, it will explode."
 ch_Teacher "If something happens, come to me at once. I'll be in the office. If something happens to me, the class rep will be your leader."

 "The HR teacher was getting out of the classroom and stopped."

 #담임 선생님 : 아 참. 학교 밖은 빠져나가지 못한다는 점을 유의해라. 나는 이만 교무실로 내려가서 이 밤을 끝낼 방법을 찾아보마.
 ch_Teacher "Oh, right. Remember that you cannot get out of the school. I'll go down to the office to find a way to resolve this problem."

 #반아이들 :...네!
 ch_Classmates "...Okay!"

 #(S) 문이 열렸다가 닫히는 소리.
 play sound "sfx/4.mp3"
 #담임 선생님은 출석부를 들고 교실을 빠져나갔다. 트레이가 입을 열자, 시선이 그에게 집중된다.
 "The teacher took the attendance book and left the classroom. Trey opened his mouth, and everyone looked at him."

 #트레이 : 뭉치면 살고, 흩어지면 죽는다 라는 말 다들 알지? 우리도 이곳에서 탈출하기 위해 서는 뭉쳐야 해. 이곳은 위험하니깐 안전한 곳을 찾아보자. 일단 나를 선두로 모두 날 따라오도록 해.
 ch_Trey "'United we stand, divided we fall.', we all know what it means. We have to stick together to get out of here. This place is dangerous, so let's try to find a safe place. Follow me."

 #트레이는 말을 마친 후 교실을 빠져나갔고, 아이들도 서로 눈치를 보더니 따라 나갔다.
 "Trey left the classroom after he finished speaking, and the rest of the class followed him."

 scene pl8 with fade

 #리엘 : 밤...? 메두사...? 다들 무슨 소리를 하고 있는 거지? 그리고 살아있는 아이들! 혹시 이 건 꿈인 걸까…….
 ch_Riel "What? Medusa...? What the hell are they talking about? And how is everyone all alive? This must be all a dream.."

 #나는 잠시 눈을 감고, 꿈에서 깨보려고 했다. 하지만 온 몸에서 이것은 꿈이 아니라는 것을 말해주고 있었다.
 "I closed my eyes, and tried to wake up. I realized none of this was a dream. "

 #리엘 : 이럴 때가 아니야. 리나!! 리나를 찾으러 가야해..!
 ch_Riel "This is not the time for this. Lina!! I have to find Lina...!"

 #S#9. INT. 2-5 / 밤
 scene pl9 with fade

 show Riel a angry at center with dissolve

 #리엘 : 리나!!!
 ch_Riel "Lina!!"

 #리나를 부르며 교실문을 세게 박차고 들어왔지만, 교실은 텅 비어있다.
 "I walked in rashly shouting Lina's name, but the classroom was empty."

 show Riel a idle at center

 #리엘 : 아무도 없잖아..? 잠만 저건!
 ch_Riel "Nobody's here...? Wait, That's..!"

 show il14 with fade
 #(머리핀 클로즈업.)

 #바닥에 떨어져있는 머리핀을 주웠다.

 #리엘 : 이건 리나의 머리핀이잖아?
 ch_Riel "This is Lina's hairpin"

 hide Riel with dissolve

 #서둘러 리나의 자리로 다가갔다.
 "I went to Lina's seat in a heartbeat"

 #(배경 리나의 책상. 그 위에는 리나의 이름이 적힌 음악책이 올려져 있다.)
 show il15 with fade

 #음악책..?
 "Music book..?"

 menu:
    "Go to music room.":
     jump menu1
    "Chase Trey even if it is late.":
     jump menu2
    "Just forget everything and wait here.":
     jump menu3

 return



 #10_1 음악실에 간다.

 #10_2 트레이를 뒤늦게라도 쫓아간다.

 #10_3 그냥 모든 걸 포기하고, 여기서 기다리자.

label menu1:

 #S#10_1. 리엘 : 리나가 음악실에 있을 지도 몰라! 음악실로 가보자.
 ch_Riel "Maybe Lina's in the music room! Let's go there."

 #INT. 음악실 / 밤
 scene pl10 with fade

 #하지만 음악실에는 아무도 없다.
 "But there is nobody in the music room."

 show Riel a idle at center with dissolve

 #리엘 : 또 아무도 없어.
 ch_Riel "No one's here either."


 #아무래도 다른 곳에 가봐야겠다. 음악실 문을 열고 나가려는데..
 "I should go to somewhere else. As Riel tries to get out of the music room..."

 hide Riel with dissolve

 #리엘 : 어?! 으악!
 ch_Riel "huh?! Ahh!"

 #음악실을 나가려고 했지만, 누군가의 거센 밀침에 음악실에 다시 밀려들어가게 되었다.
 "I tried to get out of there, but I was pushed back to the music room by somebody's big push."



 jump music

 return

label menu2:

 #S#10_2 리엘 : 리나도 리나지만, 일단 반 아이들이랑 함께 해야지. 뭉치면 산다고 그러잖아.
 ch_Riel "Lina is important for me, but I have to stick together with the guys.It would be much safer that way."

 #INT. 복도 / 밤
 scene pl11 with fade

 #하지만 복도는 텅 비어있다.
 "But the hallway is empty."

 show Riel a solid at center with dissolve

 #리엘 : 다들 어디로 간 거지..? 아무도 보이지가 않네. 반대편으로 돌아 가볼까?
 ch_Riel "Where did everyone go? I can't see anyone here. Should I go back to the other side?"

 hide Riel with dissolve

 #...어? 으악!
 ch_Riel "...uh? Ahh!"

 #반대편으로 돌아가려고 했지만, 갑자기 뒤에서 세게 미는 바람에 얼떨결에 음악실에 들어가게 되었다.
 "I tried to go back to the other side, but suddenly somebody pushed me back to the music room"

 jump music

 return

label menu3:

 #S#10_3 리엘 : 무서워…그냥 여기에 있자.
 ch_Riel "I'm scared ... Let's just stay here."

 #INT. 2-3/ 밤
 scene pl12 with fade


 #한참을 자리에 앉아, 누군가가 오기를 기다렸다.
 "I sat for a long time and waited for someone to come."

 #(S) 발걸음 소리
 play sound "sfx/5.mp3"
 show Riel a idle with dissolve
 play sound "sfx/5.mp3"
 #리엘 : !!누군가 오고 있어. 문을 열어주자.
 ch_Riel "Somebody's coming. Let's open the door!!"

 hide Riel with dissolve

 show il16 with fade

 #나는 문을 열었고… 비명을 지를 틈도 없이, 눈 앞은 붉은색으로 물들었다.
 "I opened the door... All of a sudden, everything turned red."

 return
 #▶베드 엔딩1 <빠른 죽음>


label music:

 play music "bgm/5.mp3"

 #S#11. INT. 음악실 / 밤
 scene pl13 with fade

 #나를 민 손길의 주인공은 오스카다. 왜 이런 짓을... 오스카의 얼굴은 땀으로 범벅 되어있다.
 "Oscar was the one who pushed my back. Why would he do such a thing.. Oscar's face was covered with sweat."

 show Oscar a surp at left with dissolve

 show Riel a surp at right with dissolve

 show Riel a angry at right

 #리엘 : 뭐 하는 거야?
 ch_Riel "What the hell are you doing?"

 show Oscar a mental at left

 #오스카 : 너야말로 겁도 없이 밖을 살피지도 않고, 왜 문을 여는 거지? 밖에 메두사가 있었다고.
 ch_Oscar "You're the one who carelessly opened the door. There was a Medusa outside."

 show Riel a idle at right

 #리엘 : 메두사...?
 ch_Riel "A Medusa ...?"

 show Oscar a idle at left

 #오스카 : 그래. 지금 우리 학교에는 메두사가 아이들을 잡아 먹으면서 돌아다니고 있잖아.
 ch_Oscar "Yeah. The Medusa is wandering around to eat everyone."

 show Riel a solid at right

 #리엘 : 밖에 메두사가 있다고?
 ch_Riel "Are you saying there's a Medusa outside?"

 #오스카 : 메두사가 근처에 있으면 붉은 그림자가 져. 넌 도대체 이것도 모르고 아직까지 어떻 게 살아있는 거냐.
 ch_Oscar "Your surrounding will turn red when the Medusa is around. You're lucky that you're still alive."

 show Riel a idle at right

 #리엘 : (눈이 커지며) 밖에 우리 반 애들이 있어...! 리나도..혹시 모른다고!!
 ch_Riel "But.. our friends are still out there..! Lina... might be there too!!!"

 hide Oscar with dissolve
 hide Riel with dissolve

 show b with fade

 #뛰쳐나가려는 나를 오스카가 빠르게 붙잡았다. 오스카를 뿌리치려고 했지만, 얼마나 세게 붙잡았는지 뿌리쳐지지가 않는다.
 "Oscar quickly stopped me from getting out. I tried to shake him off, but it didn't work."

 #오스카 : 죽고 싶어서 환장을 한 거야? 나까지 죽고 싶지 않으니 가만히 있어.
 ch_Oscar "Now you're acting suicidal. I don't want to die with you, so calm down."

 #리엘 : 하지만...!!
 ch_Riel "But...!!"

 #(S) 비명소리.

 scene pl13 with fade


 show Oscar a solid at left with dissolve
 show Riel a idle at right with dissolve


 #리엘 : ....
 ch_Riel "...."

 #오스카 : ....거봐.
 ch_Oscar "....Told you."

 #리엘 : ....
 ch_Riel "...."


 #(S) 오디오 잡음 소리.


 #: 지지...직... 희생자. 2학년 3반 라옹, 후센, 아노, 요노.…….
 ch_Audio "tzzz...zzz... The victims. 11th grade, third class Raon, Fusen, Ano, Yono .... ... ."


 show Riel a surp at right


 #리엘 : (충격 받은 얼굴로) 우리 반 애들이잖아....
 ch_Riel "Those are the guys from our class..."

 show Oscar a envy at left

 #오스카 : 나 덕분에 안 죽은 걸 다행이라 생각해.
 ch_Oscar "You should really thank me that you're still alive."

 show Riel a solid at right

 #리엘 : 이 상황에 그런 말이 나와?
 ch_Riel "This is not the time for that."

 show Oscar a solid at left

 #오스카 : (냉정하게) 그런 대체 무슨 말을 해야 하지? 슬프다? 정신 차려. 이 밤이 어떻게 시 작 되었는지는 모르겠지만, 쟤네들은 안타깝지만 이미 죽은 애들이야. 남보다는 내 자신이 여 기를 빠져나가는 게 관건이라고. 괜한 동정만 가졌다가 죽기 십상이야.
 ch_Oscar "What the hell was I supposed to say? That I feel sad for those guys? Get your shit together man"

 show Oscar a idle at left

 ch_Oscar "I don't know how all of this happened, but we can't do anything about people who are already dead. What matters is that we get out of here safely. Mourning for them won't do anything"



 show Riel a idle at right

 #리엘 : ...
 ch_Riel "..."

 show Oscar a smile at left

 #오스카 : 뭐...니 여친은 죽지 않은 거 같으니, 안심하라고.
 ch_Oscar "anyway...Your girlfriend seems to be alive, so relax."

 show Riel a shy at right

 #리엘 : 여친?
 ch_Riel "Girlfriend?"

 show Oscar a shy at left

 #오스카 : 복도에서 널 도와주던 파란머리 여자애 말이야. 여자친구가 아닌 건가?
 ch_Oscar "The blue haired girl who helped you in the hallway. Isn't she your girlfriend?"

 show Riel a smile at right

 #리엘 : 사귀는 거 아니야. ...아직은.
 ch_Riel "...not yet"

 show Oscar a smile at left

 #오스카 : (살짝 웃으며) 뭐, 그래. 그렇다고 하지. 아, 밖이 좀 조용해진 거 같으니, 이제 나가 볼까?
 ch_Oscar "Well, yeah. Whatever. Oh, it's silent outside now, shall we head out?"

 hide Oscar with dissolve
 hide Riel with dissolve

 #S#12. INT. 리엘의 교실 / 밤
 show il17 with fade

 #혹시나 해서 우리반으로 와봤지만, 역시 아무도 없다. 반 아이들의 책상 위에는 국화꽃이 올려져 있다.
 "I came back to our class, but nobody was there. Flowers were placed on some of the desks."

 #리엘 : 아깐 아무 것도 없었는데...
 ch_Riel "This wasn't here before..."

 #자세히 보니 국화꽃엔 핏방울 튀겨있다.
 "Looking closer, I found that blood was spattered on the flowers"

 #메두사의 짓일까...
 "Is this the doing of the Medusa...?"

 scene pl14 with fade

 show Oscar a idle at left with dissolve
 show Riel a idle at right with dissolve

 #리엘 : 넌 이제 어디로 갈 거야?
 ch_Riel "Where are you going now?"

 show Oscar a solid at left

 #오스카 : 이 밤을 끝낼 단서를 찾으러. 우선 방송실에 가볼 거야. 거기서 방송이 나왔을 테니, 무언가가 남아 있겠지.
 ch_Oscar "To look for some clues that might get us out of here. I'll go to the broadcasting room first. That's where the broadcast came from, so something must be there."

 show Riel a solid at right

 #리엘 : 아...
 ch_Riel "Ah ...."

 show Oscar a idle at left

 #오스카 : 넌?
 ch_Oscar "You?"

 show Riel a smile at right

 #리엘 : 난 리나를 찾아야 해.
 ch_Riel "I have to find Lina."

 show Oscar a surp at left

 #오스카 : 어디에 있는지는 알고?
 ch_Oscar "Do you know where she is?"

 show Riel a idle at right

 #리엘 : 그건...
 ch_Riel "I don't know..."

 show Oscar a idle at left

 #오스카 : 어디에 있는 지도 모르면서 찾아다니는 건 죽기 딱 좋아. 너도 날 따라오던가. 이 밤 의 끝을 찾으러 가는 동안 리나가 나올 수도 있는 거잖아?
 ch_Oscar "If you're thinking about finding her without any information, you should just give up. Why don't you follow me? Maybe we'll find Lina while we are looking for the clues."

 show Riel a solid at right

 #리엘 : 그건 그렇지만...
 ch_Riel "You are right but..."

 show Oscar a envy at left

 #오스카 : 뭐, 싫으면 말고.
 ch_Oscar "Well, it's your funeral."

 show Riel a smile at right

 #리엘 : (잠시 고민을 하다가) ...좋아. 대신 리나를 찾는 것을 도와줘.
 ch_Riel "...Fine. But help me find Lina."

 hide Oscar with dissolve
 hide Riel with dissolve

 stop music

 show il19 with fade

 #그때 누군가 교실 문을 거칠게 열고 들어왔다.
 "someone opened the door of the classroom roughly."

 #트레이 : (숨을 헐떡이며) 하...흐...
 ch_Trey "Ha...Huh..."


 #트레이다. 살아있었다니!
 "It's Trey. He is alive!!"

 play music "bgm/6.mp3"

 #리엘 : 트레이...?
 ch_Riel "Trey...?"


 #트레이 : 리엘...!
 ch_Trey "Riel...!"

 scene pl14 with fade

 show Riel a angry at left with dissolve
 show Trey a idle at right with dissolve

 #리엘 : 넌 살아있었던 거야? 다른 애들은?!
 ch_Riel "You're alive! What about the other guys?!"

 show Trey a surp at right

 #트레이 : (침통하게) 다른 애들은...다...메두사에게...난 운 좋게 겨우 빠져나올 수 있었어....내 가 아이들을 끝까지 잘 챙겼어야 하는데...!
 ch_Trey "others were...they...were caught by the Medusa...I barely made out alive...I should've looked after them..!"

 #트레이는 차마 말을 잇지 못하고 울먹인다.
 "Trey couldn't finish his sentence and started crying."

 hide Riel with dissolve
 hide Trey with dissolve


 show il20 with fade


 #트레이의 어깨에 손을 올려, 그를 위로하려고 노력했다. 눈앞에서 친구들을 잃다니...트레이의 마음이 어떨 지 이해 간다.
 "I patted him on the shoulder to comfort him. Losing his friends right before his eyes...It must have hurt him so much.."

 #트레이 : 얼핏 본 메두사는 정말 끔찍했어...붉은 그림자에 둘러싸인... 그리고 피투성이의 치 마...징그러운 머리...
 ch_Trey "I only took a glimpse of the Medusa's head, and it was horrifying. Surrounded by red aura... bloody skirt...creepy hair..."

 #트레이는 상상만이라도 끔찍한지, 몸서리를 쳤다.
 "Just the hindsight of what he saw was enough to make him shudder."

 scene pl14 with fade

 show Riel a idle at left with dissolve
 show Trey a idle at right with dissolve

 #리엘 : 괜찮아?
 ch_Riel "Are you ok?"

 show Trey a solid at right

 #트레이 : 우린 도망쳐야 해. 리엘, 어디로 갈 예정이었어?
 ch_Trey "We have to get the hell out of here. Riel, where were you heading?"

 show Riel a solid at left

 #리엘 : 우린 3층 방송실. 방송이 나온 곳에 뭐가 있을 가 해서.
 ch_Riel "The broadcasting room at the 3rd floor. We thought something might be there."

 show Trey a solid at right

 #트레이 : 방송실? ...내가 방송실은 이미 다녀왔어. 문이 잠겨있던데.
 ch_Trey "The broadcasting room? ...I already went there just now. The door was locked."

 hide Riel with dissolve

 show Oscar a solid at left with dissolve

 #오스카 : 쫓기는 와중에, 3층까지 갔단 말이야?
 ch_Oscar "Hang on. You went to the 3rd floor while being chased by that freak?"

 show Oscar a angry at left

 #오스카는 눈을 가느다랗게 뜨고, 트레이를 쳐다봤다. 트레이는 오스카를 힐끗 쳐다보고, 말을 이었다.
 "Oscar stared at Trey, with his eyes slightly open.. Trey glanced at Oscar a bit and continued speaking."

 show Trey a abb at right

 #트레이 : ...도망치다 보니깐 3층이었어. 아무튼 3층에 올라가봤자, 아무 소용없을 거야. 나랑 1 층으로 가자. 교무실에 가야겠어!
 ch_Trey "...I realized I was already on 3rd floor when I got there. Anyways, it will be no use when you go to the third floor. Come with me to the ground floor. I gotta go to the office!"

 hide Trey with dissolve
 show Riel a idle at right with dissolve

 #리엘 : (오스카를 쳐다보며) 오스카. 어떻게 생각해?
 ch_Riel "Oscar. What do you think?"

 show Oscar a idle at left

 #오스카 : 난 교무실에 안 갈 거야. 리엘 너도 가고 싶으면 너 혼자 가. 게다가 아까 비명소리는 아래층에서 들린 것 같다고.
 ch_Oscar "I'm not going to the office. Riel, if you want to go, you can go alone. Besides, I think I heard scream from downstairs."


 #S#13

 show Riel a smile at right


 #리엘 : 반장의 말이니깐...! 담임 선생님을 뵈러 교무실로 가자.
 ch_Riel "I'll follow the class rep..! Let's go to the office to meet the teacher."

 hide Oscar with dissolve
 hide Riel with dissolve
 stop music

 #INT. 교무실 앞 / 밤
 play music "bgm/4.mp3"

 scene pl15 with fade


 #1층의 복도는 푸른 빛이 돈다. 그리고 조용하며, 아무도 없다. 복도의 끝에서 무언가가 튀어나와도 이상하지 않을 것 같다.
 "The hallway of the first floor seems slightly blue. It's also totally silent and empty. I wouldn't be surprised if something pops out at the end of the corridor."

 show Riel a solid at center with dissolve

 #리엘 : 음... 오스카를 두고 온 것이 찜찜하지만, 방법은 이것 밖에 없으니…
 ch_Riel "Oh well… leaving Oscar alone bugs me a little, but there is no other way.."

 hide Riel with dissolve

 #S#14. 교무실 / 밤
 scene pl16 with fade

 #트레이와 교무실로 들어왔다.
 "We entered the office with Trey."

 show Teacher a smile at left with dissolve

 #담임 선생님 : 어, 리엘아! 트레이!
 ch_Teacher "Riel! Trey!"

 show Riel a smile at right with dissolve

 #리엘 : 담임 선생님!
 ch_Riel "Teacher!"

 #담임 선생님의 얼굴을 보니, 긴장이 풀리는 기분이다. 매일 보는 얼굴인데도, 오늘 따라 더 반가운 것 같다.
 "I felt relaxed when I saw the teacher's face. I see him everyday, but given the occasion, I felt particularly relaxed."

 show Teacher a idle at left

 #담임 선생님 : 너네 라도 이렇게 만나서 다행이구나.
 ch_Teacher "I am glad to see that you're alive."

 show Riel a idle at right

 #리엘 : 다른 애들은...?
 ch_Riel "What happened to the other kids?"

 show Teacher a surp at left

 #담임 선생님 : 그게...
 ch_Teacher "The other kids were..."

 show Riel a solid at right

 #리엘 : 역시나... 그 방송이 맞았군요.
 ch_Riel "Of course.. The broadcast was right.."

 show Teacher a smile at left

 #담임 선생님 : 그래도 너희가 안전해서 마음이 조금 놓이네. 난 혹시나 다른 학생들이 날 찾 아올까봐, 여기서 기다리고 있단다.
 ch_Teacher "It relieves me that you guys are safe at least. I was waiting here in case other students needed me."

 hide Riel with dissolve

 show Trey a idle at right with dissolve

 #트레이 : 저희가 뭐 도울 것이 있나요?
 ch_Trey "Is there anything we can do to help?"

 show Teacher a idle at left

 #담임 선생님 : 분명 여기서 탈출할 수 있는 방법이 있을 거야. 음...혹시 이곳을 탈출할 수 있는 단서를 찾아주겠니?
 ch_Teacher "There must be a way to get out of here. Well...Can you go find some clues that will help us escape?"

 hide Teacher with dissolve
 hide Trey with dissolve


 #음...
 "Hmm..."



 menu:
    "Go to the library to find some clues.":
     jump book
    "Go to the third floor to find Oscar.":
     jump third
 return


 #15_1 단서를 찾기 위해 도서관으로 간다.
 #15_2 오스카를 찾으러, 3층으로 간다.


label third:

 #S#15_2. INT. 3층 복도 / 밤
 scene pl17 with fade

 #3층 복도는 썰렁하다. 오스카는 어디로 간 걸까. 우선 제일 가까이 있는 도서관으로 들어가자. (15_2)
 "The third floor hallway is cold. Where did Oscar go? First, let's get to the nearest library."


 jump book

 return

label book:

 #S#15_1. INT. 도서관 / 밤
 scene pl18 with fade


 #도서관에는 아무도 없다.
 "There is no one in the library."

 show Trey a idle at right with dissolve

 #트레이 : 책을 조사해볼까?
 ch_Trey "Why don't we investigate the books?"

 show Riel a idle at left with dissolve

 #리엘 :책이 너무 많은데 이 안에서 어떻게 찾지?
 ch_Riel "There are way too many books. How are we supposed to find anything from here?"

 show Trey a smile at right

 #트레이 : 학교소개란 쪽을 찾아보자.
 ch_Trey "Let's look at the school description page."

 hide Riel with dissolve
 hide Trey with dissolve

 #.
 "."
 #.
 ".."

 show Riel a idle at left with dissolve

 #리엘 :　뭐지. 아무 것도 없잖아
 ch_Riel "Huh. Nothing."

 show Trey a idle at right with dissolve

 #트레이 :　그러게.
 ch_Trey "Yeah. Nothing."

 show Riel a solid at left

 #리엘 : 이상할 정도로 아무 것도 없는데... 보통 학교 건립소개, 교사진소개 같은 것쯤은 나와 있지 않나...
 ch_Riel "It's weird that there's nothing at all. Don't description pages have information about the history of the school or the faculty usually? "

 show Trey a abb at right

 #트레이 : 아무튼 여기서 얻을 수 있는 정보는 없는 것 같아. 옆 교실로 가보자.
 ch_Trey "I doubt we can get any information from here. let's move on and go to the next classroom."

 hide Riel with dissolve
 hide Trey with dissolve
 stop music

 #과학실로 이동한다.(16)


 jump science

 return


label science:

 #S#16. INT. 과학실 / 밤
 play music "bgm/7.mp3"
 scene pl19 with fade

 show Riel a idle at left with dissolve

 #리엘 : 여기도 아무도 없네. 오스카도 없고...
 ch_Riel "no one here either. No Oscar ..."

 show Trey a idle at right with dissolve

 #트레이 : 이렇게 어두울 때, 과학실에 오니깐 기분이 좀 그러네...
 ch_Trey "It sure is scary to come to the science lab when it's so dark."

 hide Riel with dissolve
 hide Trey with dissolve

 #화학용품냄새가 배여 있는 과학실은 서늘하다.
 "The science room with the smell of chemical products is so... ominous."

 #과학실의 신체모형이 눈이 뚫린 채로 쳐다보고 있는 것 같다. 불규칙하게 놓여있는 실험도구들도 기분이 나쁘다.
 "The human body model of the science room looks like it's staring at us.The irregularly placed experimental tools are also unsettling."

 #리엘 : 근데 과학실에 원래 이런 것이 있었나? 처음 보는 용품 같은데.
 ch_Riel "Wait, was there something like this in the science room? I've never seen this before."

 #이상한 형태의 주사기, 과학실에서 이런 걸 쓰지 않았는데... 갑자기 뒤에서 목소리가 들린다. 오스카?
 "A syringe in a strange shape. We never used such a thing in the science lab... Suddenly, I heard a voice from behind. Oscar?"

 show Oscar a idle at left with dissolve

 #오스카 : 이상할 수밖에.
 ch_Oscar "Weird, isn't it?"

 show Riel a idle at right with dissolve

 #리엘 : 오스카! 대체 어디에 있었어?
 ch_Riel "Oscar! Where the hell have you been?"

 show Oscar a angry at left

 #오스카 : 여기 원래 학교가 아니었으니깐.
 ch_Oscar "This place wasn't a school originally"

 show Riel a surp at right

 #트레이 : 무슨 소리야?
 ch_Trey "What are you talking about?"

 show Oscar a solid at left

 #오스카 : 우린 컴퓨터실에 있었어. 그리고 그렇게 큰 소리로 돌아다니면 메두사가 여기 있구 나 하고 쫓아오겠다.
 ch_Oscar "We were in the computer room. You better not walk around so loudly like that, or Medusa will find us."

 show Riel a idle at right

 #아... 무언가를 찾아내려는 것에 급급하여 소음을 생각하지 못했다.
 "Ah... I was so preoccupied with finding a clue that I couldn't think about the noise."

 show Oscar a smile at left

 #오스카 : 컴퓨터실로 따라와. 보여줄 게 있으니.
 ch_Oscar "Follow me to the computer room. I have something to show you."

 hide Oscar with dissolve
 hide Riel with dissolve


 #S#17. INT. 컴퓨터실 / 밤
 show pl20 with fade


 show il22 with fade

 #컴퓨터실에 가자, 한 여학생이 켜져 있는 컴퓨터 앞에 앉아 있다.
 "When we entered the computer room, we saw a girl sitting in front of the computer."

 #오스카 : 얜 제인이야. 아까 3층에서 만났어.
 ch_Oscar "It's Jane .I met her on the third floor."

 #트레이 : (웃으며) 안녕?
 ch_Trey "Hi..."

 #제인 : (얼굴을 붉히며) 안녕...
 ch_Jane "Hi..."

 #리엘 : 계속 혼자 있었던 거야?
 ch_Riel "Have you been alone the whole time?"

 #제인 : 원래 급식실에서 다 같이 있었는데, 일진무리들이 음식을 독차지하고 애들을 괴롭히는 바람에...                                                                                                                                                              리엘 : 아...
 ch_Jane "I was in the cafeteria with everyone, but the bullies took all foods and caused a scene.."

 #제인 : 아마 다른 애들은 급식실에 다 같이 있을 거야!
 ch_Jane "Everyone's probably still in the cafeteria!"

 #트레이 : 근데 이건 뭐야?
 ch_Trey "Anyways, what's this?"


 show il24 with fade

 #트레이는 켜져 있는 컴퓨터화면을 가리킨다.
 "Trey points to the computer screen."

 #화면은 파랗게 빛나고 있다. 나도 궁금했던 터, 오스카를 바라봤다.
 "The screen is blue. I was curious about it too, so I looked at Oscar."

 #오스카 : 우리도 너희처럼 이 밤을 벗어날 방법을 찾고 있었어. 이건 내가 컴퓨터실을 조사하 다가 찾아낸 거. 20년 전 자료야.
 ch_Oscar "We were looking for ways to end this whole thing just like you guys. This is what I found here. It's documented 20 years ago."

 #리엘 : 20년 전...?
 ch_Riel "20 years ago?"

 #트레이 : 이건 지도처럼 보이는데.
 ch_Trey "It looks like a map."

 #오스카 : 맞아, 지도. 이 건물의 지도가 나와 있지.
 ch_Oscar "Yup, it's a map. A map of this building."

 #트레이 : 하지만 위치가 좀 다른 것 같은데?
 ch_Trey "But it looks a little different."

 #오스카 : 그게 중요한 점이야. 여기에 써져 있는 건 교실이 아닌 연구실 넘버.
 ch_Oscar "That's the important part. Instead of the classrooms, there are laboratories."

 #제인 : 그래서 나랑 오스카는 학교가 세워 지기 전 연구소가 아니었을 까라는 추측을 하고 있어. 여기에 연구원들이 남긴 일지도 있고.
 ch_Jane "So Oscar and I were speculating that the school was a research facility before. You can even see journals left by the researchers."

 scene il25 with fade

 #메시지? 음....
 "A Journal? Hmm..."

 #‘19xx. x.x 넘버137 오늘 실험은 매우 성공적이었다. 조금만 아주 조금만 더 한다면 대표님 말처럼 실체화가 가능할지도... 우린 할 수 있을 것이다.’
 "'19xx. xx Experiment Number 137 was very successful. At this rate, we might be able to bring it to life soon as the boss said ... We can do it. '"

 #.... 우리 학교가 연구소이었다니... 처음 듣는 소리다.
 ".... Our school was a research facility...I never knew."

 #트레이 : 새로운 사실이야. 우리한테 알려줘서 고마워. 리엘, 담임선생님께 알려드리러 가자.
 ch_Trey "It's a news for us. Thanks for letting us know. Riel, let's tell this to our teacher."


 menu:
    "Go to HR teacher.":
     stop music
     jump hr
    "Go somewhere else.":
     stop music
     jump some
 return

 #18_1 담임선생님께 간다.


 #18_2 다른 곳을 가본다.



label hr:

 #S#18_1.
 play music "bgm/8.mp3"


 #오스카 : 우리 학교가 연구소이었다는 걸 알려드려서 뭐 하려고. 선생님은 이미 알고 계실 가능성이 더 클 걸?
 ch_Oscar "What's the point of telling him that our school was a research facility? He probably already knows about it."


 #맞는 말이다. 좀 더 알아보자. (19로)
 "You're right. Let's investigate a little bit more."

 jump floor


 return


label some:

 play music "bgm/8.mp3"




 #S# 18_2


 scene pl20 with fade



 show Riel a idle at left with dissolve

 #리엘 : 조금 더 찾아보고, 담임 선생님에게 가자.
 ch_Riel "Lets look a little further, and then go to our teacher."



 #INT. 방송실 / 밤

 show Trey a idle at right with dissolve

 #트레이 : 그렇다면...나 혼자 담임 선생님에게 가볼게. 트레이는 혼자 계단을 내려갔다.
 ch_Trey "If that's the case...I will go tell our teacher on my own."

 hide Riel with dissolve
 hide Trey with dissolve

 "Trey went down the stairs alone."

 show Oscar a smile at left with dissolve

 #오스카 : 우린 방송실로 가볼까? 아까 지나가면서 확인해보니, 문이 열려 있더라고.
 ch_Oscar "Should we go to the broadcasting room? The last time I checked, the door was open."

 show Jane a smile at right with dissolve

 #제인 : 거기서 뭘 알아낼 수 있을 지도 몰라.
 ch_Jane "We might be able to find something out there."

 hide Oscar with dissolve
 hide Jane with dissolve


 scene pl21 with fade


 #오스카의 말대로 우린 방송실로 들어왔다.
 "As Oscar said, we came into the broadcast station."


 #(S) 오디오 잡음소리


 #방송실에 들어오자 마자, 교실의 방송기계에서는 오디오소리가 작게 반복해서 나고 있다.
 "As soon as I entered the broadcasting room, I could hear a faint sound repeated from the broadcasting machine."

 show Oscar a solid at left with dissolve


 #오스카 : 이건 뭔 소리지?
 ch_Oscar "What is this sound?"

 show Riel a idle at right with dissolve

 #리엘 : ..!! 소리 좀 키워봐.
 ch_Riel "...!! Make it louder."

 #제인은 소리를 키웠다. 음성이 좀 더 크게 들린다.
 "Jane raised the sound. It was easier to hear the sound."

 #??? : 여기는 2학년 5반. 지금 당장 오지 않는다면, 네 여자친구인 리나는…….
 ch_unknown "This is the 11st grade, fifth class.If you don't come right now, your girlfriend Lina will..."

 #이건.. 내가 학교에 오기 전 왔던 전화소리... 이 전화로 학교에서의 밤이 시작되었다. 리나야... 바로 찾지 못해서 미안해...
 "This sound is... it's the phone call that I received before I came to school...Everything started from this phone call. Lina ... I'm sorry I could not find you right away ..."

 #.. .
 "..."

 show Oscar a idle at left

 #오스카 : 잠깐. 끝에 무슨 소리가 더 들리는 거 같은데.
 ch_Oscar "Wait. I think there's more at the end."

 show Riel a solid at right

 #리엘 : 나도 그렇게 생각해. 이거 더 잘 들리게는 할 수 없을까?
 ch_Riel "Oscar is right. Can we make it more clear?"

 hide Riel with dissolve
 show Jane a smile at right with dissolve

 #제인 : 나!
 ch_Jane "Me!"

 #(모두의 시선이 집중되자, 제인의 얼굴을 붉어진다.)

 show Jane a shy2 at right

 #제인 : 나 방송부였어...잠깐만.
 ch_Jane "I was a part of a broadcasting team...Wait a minute."

 #제인이 기계를 몇 번 만지작거리자, 리나의 목소리가 뚜렷하게 들린다.
 "Jane touched the machine a couple of times, and Lina's voice could be heard clearly from the machine."

 #리나 : 지하...나 지하에 있어...!
 ch_Lina "Basement...I'm in the basement ...!"

 hide Jane with dissolve

 show Riel a angry at right with dissolve

 #리엘 : ...! 지하? 지금 당장!!
 ch_Riel "...! Basement? We gotta go right now!!"

 show Riel a notfunny at right

 #제인 : (시무룩하게) 하지만 우리 학교에는 지하가 없는 걸...
 ch_Jane "But our school does not have a basement..."

 show Oscar a smile at left

 #오스카 : 있을 지도 모르지. 지하에 대해서도 찾아 봐야 겠어.
 ch_Oscar "Maybe there is. We should see if there's a basement."

 #우리 학교에 숨겨져 있던 게 이렇게 많았나...
 "There were so many things hidden in our school ..."

 #우선 리나를 찾아야 해..
 "First we have to find Lina"

 show Riel a idle at right

 #리엘 : 아까 지도를 참고하며, 1층에서 지하를 찾아보자
 ch_Riel "Let's find the entrance to the basement from the first floor."

 hide Oscar with dissolve
 hide Riel with dissolve

 jump floor


 return




label floor:

 #S#19. 1층복도 / 밤
 scene pl22 with fade

 #어디로 가지?
 "Where should we go?"




 menu:
    "School office":
      jump office
    "School Cafeteria":
      jump cafe

 return



 #20_1. 교무실


 #20_2. 급식실



label office:

 #S#20_1. 교무실 / 밤
 scene pl23 with fade


 #(S) 문열리는 소리
 play sound "sfx/8.mp3"
 show Jane a surp at right with dissolve


 #제인 : (인상을 찌푸리며) 으.. 냄새..
 ch_Jane "Ugh ... It stinks.."


 #제인의 말대로 교무실 안에는 지독한 냄새로 가득했다.
 "As Jane said, the office was filled with a terrible smell."

 show Riel a surp at left with dissolve

 #리엘 : 이건…?!
 ch_Riel "What the...?!"

 hide Jane with dissolve
 hide Riel with dissolve


 show il26 with fade


 #내 발끝에 닿은 것은 트레이와 담임선생님이었다.
 "It was Trey and our HR teacher who reached my toe."

 #리엘 : 트레이…? 왜 여기서…!
 ch_Riel " Trey...? Why is he....!"

 #오스카 : 리엘! 뒤에!
 ch_Oscar "Riel! behind!"

 show il27 with vpunch

 #오스카의 다급한 말에 급하게 뒤를 돌아봤지만, 무언가가 내 뒤통수를 가격한 후였다…
 "I tried to look back after Oscar's words, but I was hit in the back of my head by something ..."

 $ achievement.grant("Mysterious Death")
 $ achievement.Sync()


 scene black with hpunch

 #아…
 "Ah…"

 stop music

 #.


 #.
 #▶베드 엔딩2 <잘못된 선택>


 return




label cafe:

 stop music

 play music "bgm/9.mp3"


 #S#20_2.

 #우선 내가 할 수 있는 일들을 해보자. 지하로 가는 통로는 1층에 있을 거야.
 "Let's start what I can do. The passage to the basement will be on the first floor."


 #INT. 급식실 / 밤
 scene pl24 with fade


 #급식실 문을 여는 순간, 시끄럽던 내부가 급격하게 조용해졌다.
 "As soon as I opened the door, the loud room suddenly became quiet."

 #왜 이렇게 다들 경계를 하는 거지...?
 "What's going on here?"

 show Riel a smile at left with dissolve

 #리엘 : (조심스럽게) 안녕?
 ch_Riel "Hi."

 show Student1 a idle at right with dissolve

 #일진1 : 뭐야?
 ch_Student1 "What do you want?"

 hide Student1 with dissolve

 show Riel a idle at left

 #리엘 : 같이 이야기를 하면 좋을 것 같아서 왔는데.
 ch_Riel "I thought it would be helpful to share some information."

 show Student2 a idle at right with dissolve

 #일진2 : 그래서?
 ch_Student2 "So?"

 show Riel a solid at left

 #리엘 : 우리 같이 탈출하는 방법을 찾아보는 게 어때? 우리 다 같이 힘을 합치면 충분히 탈출 할 수 있을 거야.
 ch_Riel "Why don't we find a way out together? If we all unite, we'll be able to escape."

 show Student2 a pet at right

 #일진2 : 어떻게?
 ch_Student2 "How?"

 show Riel a idle at left

 #리엘 : 응?...그건...우리도 아직 잘...하지만 금방 찾을 수 있을 거야. 그리고 우리가 먹은 게 없이 도망만 다녀서 그러는데, 먹을 것 좀 줄 수 있을까?
 ch_Riel "Uh...Umm...At this moment, we don't know...But we will able to figure it out soon."

 show Riel a smile at left
 ch_Riel "Also, we had to run away from the Medusa without eating anything, could you share some food for us?"

 hide Student2 with dissolve

 show Student1 a pet at right with dissolve

 #일진1 : 결국은 탈출할 방법은 찾지 못했으면서, 먹을 거는 가져가겠다는 거 아니야. 지금 함부로 돌아다니다가, 죽기 십상이야. 우린 여기서 기다리면서, 구조를 기다릴 거라고.
 ch_Student1 "Oh, you didn't figure out a way to escape, but you're trying to grab our food?"

 show Riel a solid at left

 show Student1 a angry at right

 ch_Student1 "It would be suicidal to walk around so carelessly. We'll wait here for the rescue."

 hide Student1 with dissolve

 show Student2 a pet at right with dissolve

 #일진2 : 너희에게 줄 식량 따윈 없으니깐, 꺼져.
 ch_Student2 "There is no food for you. Now, get lost."

 #기대했던 것과는 다르게 급식실의 아이들의 반응은 냉담했다.
 "Unlike what we expected, we were faced with a cold response"

 show Riel a idle at left

 #리엘 : 하지만!!
 ch_Riel "But!"

 hide Riel with dissolve
 hide Student2 with dissolve

 show Oscar a angry at left with dissolve

 #오스카 : 됐어. 말이 안 통한 이기적인 부류야. 이야기할 가치도 없어.
 ch_Oscar "Enough. Nothing's gonna change their selfish minds. It is not even worth it."

 hide Oscar with dissolve

 #가자. 오스카는 화가 났는지, 쌩하니 급식실을 나가버렸다.
 "Let's Go. Oscar left the cafeteria because he was upset and angry."

 show Jane a solid at left with dissolve

 #제인 : 리엘....가자..
 ch_Jane "Riel...Let's go..."

 show Student1 a angry at right with dissolve

 #일진1 : 빨리 안 꺼져?
 ch_Student1 "I said get lost!"

 show Jane a surp at left

 #제인 : 꺄앗!
 ch_Jane "Ouch!"

 hide Jane with dissolve
 hide Student1 with dissolve

 #일진의 밀침에, 제인은 넘어져버렸다.
 "Jane was knocked down by the push of the bully."

 show Riel a angry at left with dissolve

 #리엘 : 괜찮아? 이 자식들이...!
 ch_Riel "Are you okay? You bastards...!!"

 show Jane a solid at right with dissolve

 #제인 : 난 괜찮으니깐, 얼른 나가자...무서워..
 ch_Jane "I'm fine, let's go... I'm scared.."


 hide Riel with dissolve
 hide Jane with dissolve


 show il28 with fade
 #제인의 다리에서는 피가 나고 있다. 난 제인을 부축해서 급식실을 빠져 나왔다.
 "Jane's leg is bleeding.I helped Jane get out of the cafeteria."

 #S#21. 양호실 / 밤
 scene pl25 with fade

 #제인의 다친 부분을 치료하기 위해, 옆 교실인 양호실로 들어왔다.
 "To heal Jane's wound, we went into the infirmary, which was right next to the cafeteria."

 #새하얀 양호실이 바깥과 대비된다. 갑자기 밝은 곳으로 들어오니, 눈이 부신다.
 "The pure white color of the infirmary contrasts with the outside. Coming to a bright spot so suddenly made my eyes hurt."

 show Oscar a idle at left with dissolve

 #오스카 : 여기 앉아.
 ch_Oscar "Sit here."

 show Jane a shy at right with dissolve

 #제인 : 내가 해도 되는데...
 ch_Jane "I can do this alone..."

 show Oscar a solid at left

 #오스카 : 됐어. 내가 해줄 테니깐 가만히 있어.
 ch_Oscar "Stay still. I'll do it for you."

 #사람의 체취가 느껴지는 것이, 누군가가 방금 전까지 있었던 것 같다. 커튼이 쳐져있는 양호실침대가 거슬린다.
 "Judging by the smell, it seems like somebody was here just before. The bed covered by the infirmary curtains seems suspicious."

 hide Oscar with dissolve
 hide Jane with dissolve



 menu:
    "This is none of my business.":
      jump nocut
    "Open the curtain.":
      jump cut

 return



 #22_1 냅둔다.
 #22_2 커튼을 열어본다.


label cut:

 #뭔가 이상한데...열어볼까?
 "Something is strange ...Should I open it?"

 show il29 with fade

 #리엘 : (놀라며) ...!!
 ch_Riel "...!!"

 #침대에는 양호선생님이 피를 흘린 채, 누워있다.
 "On the bed, there was a body of the school nurse lying down with blood around."

 menu:
    "Look closer. I need to examine further.":
      jump rescue
    "Run away.":
      jump nocut

 return

 #22_3 가까이 간다. 좀 더 확실하게 확인해 봐야겠어.
 #22_1 도망친다.


label rescue:

 # S#22_3 양호실 / 밤

 show il30 with fade

 #리엘 : (인상을 찌푸리며) 으....
 ch_Riel "Uh..."

 #양호선생님의 목에 손을 가까이 대봤지만, 아무런 떨림도 느껴지지 않는다.
 "I put my hand on the nurse's neck, but I couldn't feel anything."

 #자세히 보니 양호선생님은 메두사에게 당한 것이 아닌 것 같다.
 "It seems that the nurse was not attacked by the Medusa."

 #양호선생님의 목에 난 손자국으로 보아, 누군가가 양호선생님을 목을 졸라서 죽인 것 같은 데... 대체 누가...하지만 그것이 누군지는 알 수 없다.
 "It seems to me that somebody killed her by strangling her neck... Who the hell ...would do this?"

 #리엘 : 어? 이건 뭐지..?
 ch_Riel "Huh? What is this..?"

 show il31 with fade

 #양호선생님은 손에 노란 포스트잇을 쥐고 있다. 난 양호선생님이 쥐고 있는 노란 포스트잇을 읽었다.
 "The nurse was holding a yellow sticky memo paper.I took the sticky memo from her hand and read it."


 #...!!
 "... !!"

 #리엘 : 우리 급식실로 다시 가야 할 것 같아! (23_1로)
 ch_Riel "I think we should go back to cafeteria!"


 jump eatstore

 return


label nocut:

 #S#22_1. 괜히 열어봤다가, 못 볼 것을 볼 것 같다. 아이들보고 양호실을 나오자고 했다.
 "I should have not opened it. It was better left unseen. I suggested that we get out of the infirmary."

 #INT.1층 복도 / 밤
 show il32 with fade

 #양호실을 빠져 나오려는데, 발 밀에 노란 포스트잇 한 장이 떨어졌다. 뭐지? 하지만 여기서 포스트잇을 확인하기에는 위험한 걸... 어디로 갈까?
 "While I was getting out of the infirmary, a yellow sticky memo page fell to the ground. What is this? But I need to get out of here first..where should I go?"

 #23_1 급식실
 stop music

 jump eatstore

 return


label eatstore:

 #S#23_1. INT. 급식실 / 밤
 play music "bgm/4.mp3"
 scene pl27 with fade


 show Riel a idle at left with dissolve

 #리엘 : 급식 실에 아이들이 많았으니, 위험하진 않을 거야. 게다가 이게 힌트라면 같이 힘을 합 칠 수 있을 테니... 급식실은 방금 전과 대조되게 아주 조용하다.
 ch_Riel "The cafeteria was crowded, so it would be pretty safe there.Also, if this turns out to be a clue for us to escape from here, I may be able to get some help from the bullies."

 "Unlike before, the cafeteria was awfully quiet."

 show Jane a surp at right with dissolve

 #제인 : (인상을 찌푸리며) 으....이게 무슨 냄새야. 급식 실 문을 열자마자, 비린내가 진동한다.
 ch_Jane "....What the hell is this smell? As soon as the door was opened, I could smell a foul stench."

 hide Riel with dissolve
 hide Jane with dissolve

 show Oscar a surp at left with dissolve

 #오스카 : ...이 냄새는...
 ch_Oscar "...This smell ..."

 #이 냄새는 우리보고 더 이상 앞으로 가지 말라고 이야기하는 것 같았다. 하지만...
 "It felt like the smell was a warning to tell us not to go any further. But..."

 show Riel a solid at right with dissolve

 #리엘 : 포스트잇에는 ‘먹이용 고기 2-3#7’라고 써져 있었어. 이건 급식실의 냉장고에서 쓰이는 넘버일 거야.
 ch_Riel "On the sticky memo, it said 'Meat for feeding 2-3#7'. I guess these numbers are for organizing the meat?"

 hide Oscar with dissolve
 hide Riel with dissolve

 #아이들로 가득 차 있던 급식 실은 텅 비어있었다. 다른 곳으로 간 걸까? 우린 급식 실 안쪽으로 들어갔다.
 "The cafeteria, once filled with students, was now empty. Did everybody go to another place? We went into the cafeteria."

 #제인 : 꺄악!
 ch_Jane "Kiyaaaa!"

 #제인의 비명소리에 우리는 걸음을 멈췄다.
 "Jane's scream made us stop."

 show il33 with fade

 #제인의 시선을 따라 나의 시선이 옮겨졌고, 우리 앞에 펼쳐진 광경에 헛구역질이 나올 수 밖 에 없었다.
 "I looked at where Jane's eyes were on, and what I saw almost made us throw up."

 #오스카 : 윽
 ch_Oscar "Yuk"

 #시체다. 누가 누군지 형체를 알아볼 수 없을 정도로 찢긴 상태로 죽어있다. 아마 아까의...급식 실에 있던 아이들인 듯하다.
 "They were corpses. They were torn apart to the point it was difficult to even identify them. They probably..were the kids from the cafeteria earlier."

 #리엘 : 세상에.
 ch_Riel "For God's sake."

 #제인 : 너무 끔찍해. 이렇게 많은 애들이!!
 ch_Jane "It's terrible. They didn't deserve this!!"

 #리엘 : 우리 양호실에 있을 때 아무 소리도 듣지 못했는데.
 ch_Riel "But we could not hear anything when we were in the infirmary."

 #오스카 : 게다가 짧은 시간. 그 짧은 시간 안에 이렇게 많은 아이들을 이렇게 만들었어.
 ch_Oscar "It happened in so suddenly. It killed everyone in such a short time."

 #온 몸에 소름이 돋았다.
 "It sent shivers down my spine."

 #메두사의 움직임에서 나오는 소리로 피할 수 있을 것이라고 생각했는데... 게다가 아까 전, 급식실에서 쫓겨나지 않았더라면...
 "I thought it would be possible to avoid the Medusa by being wary of its moving sound... Besides, if I had not been kicked out of the cafeteria.. I would be.."

 #리엘 : ...우선 난 보관소 쪽으로 가볼게...너넨...
 ch_Riel "I'll go to the storage... You ..."

 #오스카 : 우린 먹을 거를 좀 챙겨보지.
 ch_Oscar "We'll salvage some foods."

 show il34 with fade

 #떨리는 손을 애써 감추고, 보관소로 들어왔다. 아까 급식실 아이들이 헤쳐 놓았는지, 어수선했다.
 "I tried to calm my trembling hands and went to the storage. It was a total mess. Maybe the guys that were in the cafeteria messed it up."

 #앞에 붙여진 라벨을 따라, 걸음을 옮겼다.
 "I followed the label to move along."

 #리엘 : 1 다시 2....1 – 38... 응? 2-3#7은 없는데..?
 ch_Riel "1 - 2 .... 1 - 38 ... Huh? Why don't I see 2-3#7 here..?"

 #아무리 쳐다봐도, 2-3#7은 없었다. 1에서 끝날 뿐, 어느 것도 2에서 넘어가지 않았다. 아...대체 뭐지...
 "No matter how I look, 2-3 # 7 was not there. The first number always ended in 1; none went beyond 2. Ah...What the hell ..."

 #오스카 : 우린 다 챙겼어. 너도 다 확인했으면 얼른 가자.
 ch_Oscar "We've got what we need. Let's go if you're done checking too."

 #리엘 : 그래...
 ch_Riel "Sure.."

 #오스카가 보관소에 들어와, 내게 말을 건 냈다. 그때 뒤에서 부스럭 거리는 소리가 들렸다. 설마 생존자가..!
 "Oscar came back to the storage and talked to me. It was then when I heard a rustling sound behind me. don't tell me it is survivor...!"

 #(S) 부스럭 거리는 소리


 #리엘 : !!
 ch_Riel "!!"

 show il36 with fade

 #인기척에 뒤 돌아본 아이의 모습은 처참하기 그지없었다.
 "We looked back to check the source of the rustling sound, and found student in a horrible state."

 #얼굴은 피로 덮어져 있어서 생김새가 분간이가지 않았는데, 그 상처들은 메두사가 낸 것이 아닌 것처럼 보였다. 자신의 눈을 직접 칼로 그었는지 눈 주변이 보기 흉하게 파여져 있었다.
 "His face was hard to identify as it was covered with blood. Furthermore, the wounds did not appear to be caused by the Medusa. "
 "He had his eyes torned out, which seemed to be a self-inflicted injury"

 #눈 없는 아이 : 앞에 누구 있지..? 말 소리가 들리는데.
 ch_Eyeless "Who's there? I can hear a voice."

 #리엘 : ...
 ch_Riel "..."

 #눈 없는 아이 : 너네도 이리와. 내가 도와줄게. 메두사는...눈만 안보면 된다고..! 너네도 눈만 없으면 살아날 수 있어!!
 ch_Eyeless "Come here.I will save you from all this."
 ch_Eyeless "Medusa...she can't do anything if you don't make an eye contact..! If you have no eyes, you can survive this!!"

 #눈 없는 아이의 손에는 칼이 들려 있다. 아이는 앞을 더듬더듬 손짓하며, 우리 쪽으로 기어온다.
 "The eyeless student was holding a knife. The child crawled towards us."

 #오스카 : (인상을 찌푸리며) 으... 리엘, 제인을 데리고 얼른 가자. 우린 아무런 수확도 없지 못하고, 도망치듯 급식실을 나섰다. (24로)
 ch_Oscar "Riel, take Jane with you. Let's get out of here. Without gaining any information, we ran away from the cafeteria."

 stop music

 # S#24. INT. 교무실 / 밤
 play music "bgm/5.mp3"
 scene pl28 with fade

 #지금까지의 상황을 담임 선생님께 말씀드려야 할 것 같아서, 교무실로 왔다. 하지만 교무실에는 담임 선생님이 계시지 않는 것 같다.
 "To report to my teacher what happened so far, I went back to the school office. However, he wasn't there. "


 show Oscar a idle at left with dissolve
 show Riel a idle at right with dissolve

 #리엘 : 선생님...?
 ch_Riel "Teacher ...?"

 show Oscar a solid at left

 #오스카 : 선생님은 안 계시는 거 같은데. 가만, 저기 트레이 아니야?
 ch_Oscar "I guess he is not here. Wait, isn't that Trey over there?"

 hide Riel with dissolve
 hide Oscar with dissolve

 show Trey a smile at right with dissolve

 #트레이 : 아, 너희구나. 선생님은 잠시 나가셨어. 무슨 일이야?
 ch_Trey "Oh, it's you guys. The teacher went somewhere. What's going on?"

 show Riel a idle at left with dissolve

 #리엘 : 담임 선생님께 할 말이 있어서. 넌 여기에 계속 있었어?
 ch_Riel "I have something to say to him. Were you here the whole time?"

 show Trey a idle at right

 #트레이 : 응. 담임 선생님을 도와드리려고.
 ch_Trey "Yes. I was helping him. I am the class rep after all."

 show Trey a surp at right

 #난 반장이잖아. (제인에게) 너 괜찮니?
 ch_Trey "Are you okay?"

 hide Riel with dissolve

 # 제인은 아무 것도 모르는 사람이 보기에도, 상태가 별로 좋지 않아 보인 듯 하다.
 "Anyone could tell that Jein was in a bad state."

 show Jane a sad at left with dissolve

 #제인 : ...응...근데 나 너무 무서워...메두사도 무섭지만, 아이들이 더 무서운 것 같아...
 ch_Jane "...yes...But I'm so scared ...Medusa is scary too, but I'm more scared about the students..."

 hide Jane with dissolve

 show il39 with fade

 #제인은 울먹이기 시작한다.
 "Jane begins to cry."

 #트레이 : 우..울지마..!
 ch_Trey "D...don't cry...!"

 #오스카 : 야, 울지마.
 ch_Oscar "Hey, you don't need to cry about it."

 #트레이와 오스카는 제인을 둘러싸며 달래주기 시작한다. 나까지 달래 줄 필요는 없어 보인다.
 "Trey and Oscar tried to comfort Jane. I thought it wouldn't be necessary for me to engage."

 show il40 with fade

 #리엘 : 응?
 ch_Riel "Huh?"

 #저기 저 서랍, 열려 있다. 교무실 서랍은 다  잠긴 걸로 아는데... 확인해보자.
 "The drawer was open. Every drawer in the school office was supposed to be locked... Let's check."

 #‘드르륵’
 "'Srrrr'"

 show il41 with fade

 #리엘 : 메모지들...? 흠... 뭔 말이지. 뭔가 이상해 보이는 말들인데. 아마 교장선생님의 메시지인 것 같다.
 ch_Riel "Notes ...? Hmm... What does it say? It looks rather strange. Perhaps it's a message from the principal."

 #‘먹이준비완료.’
 "'The feed is prepared.'"

 #‘상태체크12’ ‘10.14 지하실 출입금지.’
 "'Status check 12' '10.14 Forbid access to the basement.'"


 #리엘 : 10월 14일이면... 어제잖아? 대체 어떤 명령인 거지?
 ch_Riel "October 14th ... That's yesterday? What kind of order it is?"

 show il42 with fade

 #메모지 밑에는 다른 파일이 깔려 있다. 아마 연구원들의 신원이 정리 되어 있는 파일처럼 보인다.
 "There are other files underneath the note. It looks like a file that conveys the identities of researchers."

 #리엘 : 양호 선생님? ...다 우리 학교 선생님이잖아....선생님들도 연구소에 관련 있었던 걸 까...
 ch_Riel "The nurse?...These are all our school's faculties...Teachers were involved in the research institute too..."

 #이해가 잘 되지 않는다.
 "I couldn't understand a thing."

 #머릿속에서 무언가 하나가 막고 있는 것만 같다. 아..대체 뭐지?
 "It feels as if something's disturbing my thought process. Ah..What is it?"

 scene pl28 with fade


 #(S) 문 열리는 소리
 play sound "sfx/8.mp3"
 show Trey a idle at left with dissolve
 show Teacher a idle at right with dissolve

 #트레이 : 선생님!
 ch_Trey "Teacher!"

 show Teacher a smile at right

 #담임 선생님 : 너희들 여기에 다 모여 있구나. 무슨 일이라도 생겼니?
 ch_Teacher "You guys are all here. What happened to you guys?"

 hide Trey with dissolve

 show Oscar a solid at left with dissolve

 #오스카 : 그게 ……
 ch_Oscar "Uh..."

 show Teacher a surp at right

 #오스카가 지금까지 있었던 일을 이야기하기 시작한다. 이야기를 들을수록 담임 선생님의 표정이 점차 굳어간다.
 "Oscar begins to talk about what has happened so far. The teacher's face turns serious as he listens to the story."

 show Oscar a idle at left

 #...
 "..."

 show Teacher a idle at right

 #.. .
 "..."

 show Teacher a notfunny at right

 #담임 선생님 : 하...
 ch_Teacher "Ha..."

 #오스카가 이야기를 끝내자, 교무실에는 무거운 분위기가 감돌았다. 담임 선생님은 자신의 얼굴로 거칠게 쓸어 내리더니, 입을 열었다.
 "When oscar finished the story, The atmosphere of the school office turned heavy. The teacher roughly swept down his face and began to talk."

 show Teacher a solid at right

 #담임 선생님 : ...이 상황까지 왔으니, 모든 걸 이야기해줘야겠구나. 사실은 말이다...우리 학교 는...
 ch_Teacher "...At this point... I'll have to tell you everything...The fact is ...Our school was..."

 hide Oscar with dissolve
 hide Teacher with dissolve
 stop music

 #(암전) 과거회상
 scene black with fade

 #S#25. (flashback) INT. 교장실 / 오후
 play music "bgm/6.mp3"
 scene pl29 with fade

 show Principal a idle at left with dissolve

 #교장 선생님 : 어이 김 선생. 일 그 따위로 할 거야?
 ch_Principal "Hey Mr. Kim. This is how you handle things at work?"

 show Teacher a solid at right with dissolve

 #담임 선생님 : ....
 ch_Teacher "...."

 show Principal a solid at left

 #교장 선생님 : 어제 1층에서 누군가가 쿵쿵거리는 소리를 들었다는 건의가 들어왔어. 이게 어떻게 된 거야? 아직도 해결하지 못했어?
 ch_Principal "somebody reported that they heard a pounding noise from the first floor. What's going on? You still couldn't have it under control?"

 show Teacher a idle at right

 #담임 선생님 : 그게... 메두사를 어떻게 할 수가 없습니다. 그래서 지하에 가둬놓은 건데...
 ch_Teacher "That's ... I can't control the Medusa. That's why I locked it in the basement.."

 show Principal a angry at left

 #교장 선생님 : 그니깐 티가 나지 않게 해야 할 것이 아니야!!
 ch_Principal "Well, the least you could do is not make it so obvious!!"

 show Teacher a solid at right

 #담임 선생님 : 면목이 없습니다...
 ch_Teacher "You're right.. I have nothing to say.."

 show Principal a smile at left

 #교장 선생님 : 먹이는 제대로 주고 있어?
 ch_Principal "Are you even feeding it properly?"

 show Teacher a idle at right

 #담임 선생님 : 돼지고기를 주고 있는데, 그 걸로는 부족해서...
 ch_Teacher "Right now all we give is pork, but that won't be enough.."

 show Principal a solid at left

 #교장 선생님 : 김 선생, 내가 저번에 먹이를 바꾸라고 말하지 않았나?
 ch_Principal "Mr. Kim, haven't I told you to change its food?"

 show Teacher a surp at right

 #담임 선생님 : 하지만 대표님, 아니 교장선생님! 그건...!
 ch_Teacher "But, boss, I mean principal! That's..! That's...!"

 show Principal a smile at left

 #교장 선생님 : 말에 토 달지 말고, 내가 시키는 대로 하게. 음...김 선생네 반 학생들부터 먹이 로 주도록 해.
 ch_Principal "Don't talk back and do as I say. Say... Why don't you start with students from your class?"

 show Teacher a angry at right

 #담임 선생님 : 그럴 수는 없습니다.
 ch_Teacher "But sir, I can't do that."

 show Principal a solid at left

 #교장 선생님 : 이제 와서 손을 떼시겠다? 우리 실험은 더러웠지만 , 그랬기에 우리가 이 자리 까지 올라올 수 있었던 거야. 그걸 덮기 위해, 우리XX그룹에서 이 자리에 학교를 세운 거고. 자네는 이제 이 일에서 해방될 수 없네. 조금이라도 그럴 낌새라도 보였다간... 자네랑 자네가 족이 무사하지 못할 걸세.
 ch_Principal "Now you're washing hands off? I admit, our experience wasn't ethical. but it brought us where we are today. To cover it up, we XX group built a school here."
 ch_Principal "It's too late to just step out of this. If you tried to run away..We would have to kill you and your family."

 show Teacher a solid at right

 #담임 선생님 : ...
 ch_Teacher "..."

 show Principal a idle at left

 #교장 선생님 : 내 이야기를 잘 알아먹었을 것이라고 생각하지. 그럼 일 진행하도록 해.
 ch_Principal "I hope you understood what I said. Go ahead and do what I asked."

 show Teacher a idle at right

 #담임 선생님 : ... 알겠...습니다.
 ch_Teacher "... yes...sir."

 hide Principal with dissolve
 hide Teacher with dissolve

 #(flashback 완료)


 #(검정배경)
 scene black with fade

 #담임 선생님 : 우린 선생들은 XX연구소의 연구원들이었고, 교장 선생님은 거기의 대표였어. 연구소에 학교가 세워진 후, 우리의 입을 막고 메두사처리를 위해 우리를 교원으로 채용했지. 사실상 반강제적이었지만. 어쨌든...그리해서...우리 선생님들은 교장 선생님의 협박에 못 이 겨, 명령을 따른 거야...
 ch_Teacher "We were the researchers at the XX research institute, and the principal was our boss.."
 ch_Teacher "After the school was built, he tried to shut us up and hired us as teachers to take care of the Medusa. We were forced to do it"
 ch_Teacher "Anyways.. So basically... We were threatened by the principal and followed his order..."
 stop music

 #S#26. INT. 교무실 / 밤
 play music "bgm/3.mp3"
 scene pl30 with fade

 show Jane a idle at left with dissolve

 #제인 : 세상에..
 ch_Jane "Oh my God."

 show Trey a idle at right with dissolve

 #트레이 : ...
 ch_Trey "..."

 hide Jane with dissolve
 hide Trey with dissolve

 show Riel a idle at left with dissolve

 #리엘 : 그렇다면 보건 선생님도...?
 ch_Riel "So, the nurse too...?"

 show Teacher a idle at right with dissolve

 #담임 선생님 : 맞아.
 ch_Teacher "Right. She was a researcher too."

 hide Riel with dissolve

 show Oscar a idle at left with dissolve

 #오스카 : 학교에 이런 일이 일어나고 있었다니.
 ch_Oscar "Can't believe something like that was happening in our school."

 hide Oscar with dissolve
 show Riel a solid at left with dissolve

 #리엘 : 근데 교장선생님은 날 범인으로 몰았어..!
 ch_Riel "Yet the Principal accused me of murder..!"

 show Teacher a solid at right

 #담임 선생님 : 이런 일을 보고만 있었다는 것에 난 큰 죄책감을 느낀단다... 말렸어야 했는데...!
 ch_Teacher "I feel so guilty that I can't do anything about this.. I should have stopped the principal at all cost..!"

 hide Riel with dissolve
 hide Teacher with dissolve

 show il43 with fade

 #(눈물을 흘린다) 죽은 아이들에게 너무 미안하고...
 "I'm so sorry for the dead students..."

 #제인 : 선생님... 선생님도 시켜서 강제적으로 하신 일이잖아요...정말 나쁜 건 교장선생님이 죠. 이런 사람인 지도 모르고...!
 ch_Jane "Teacher ... you were also forced... The principal is to blame. If only I knew how terrible he was...!"

 #담임 선생님 : 그렇게 말해줘서 고맙구나. 이렇게 일이 된 건은 내 책임도 있으니, 지하로 가 는 방법을 알려주마. 지하로 가는 곳은 교장실 책장 뒤에 있단다. 교장실로 가자.
 ch_Teacher "Thank you for telling me that. But I bear the responsibility also. Let me tell you how to get to the basement. The entrance to the basement is behind the bookshelf in the principal's office. Let's go there."


 #담임 선생님과 교장실로 향했다.
 "We headed to the principal's office with the homeroom teacher."

 #S#27. INT. 교장실 / 밤

 scene pl31 with fade

 #담임 선생님 : 여기 책장 뒤에...
 ch_Teacher "Here, behind the bookshelf ..."

 show il44 with fade

 #담임 선생님이 책장을 빼자, 그 뒤에는 작은 문이 보인다.
 "As the homeroom teacher pulls out the bookshelf, a small door appears"

 show Oscar a solid at left with dissolve

 #오스카 : 지하로 가는 문이 여기에 있었군.
 ch_Oscar "This is the door that leads to the basement."

 show Riel a smile at right with dissolve

 #리엘 : 이 안에는 리나도 있을 거야. 얼른 가자.
 ch_Riel "I bet Lina is also there. Let's go."

 hide Oscar with dissolve
 hide Riel with dissolve

 show Jane a surp at left with dissolve

 #제인 : 잠깐만!!
 ch_Jane "Wait a second!"

 show Trey a surp at right with dissolve

 #트레이 : 밖에...
 ch_Trey "Look outside.."

 hide Jane with dissolve
 hide Trey with dissolve

 show Riel a surp at right with dissolve

 #리엘 : (놀란다)!!
 ch_Riel "!!"

 scene a with fade

 #창문에 붉은 그림자가 비치고 있다.
 "Red shadow emerges on the other side of the window."

 show il44 with fade

 show Oscar a surp at left with dissolve

 #오스카 : 메두사가 벌써...
 ch_Oscar "Medusa is already ..."

 show Riel a solid at right

 #리엘 : 서둘러야 해.
 ch_Riel "We have to hurry."

 hide Oscar with dissolve
 hide Riel with dissolve

 show Riel a idle at left with dissolve

 show Trey a solid at right with dissolve

 #트레이 : 안 돼. 여기로 내려갔다가는, 바로 잡히고 말 거야. 차라리 교장실을 탈출하는 것이 나을 지도 몰라.
 ch_Trey "No. If we go down there, we'll get caught right away. Maybe it's better to escape the principal's room."

 show Riel a angry at left

 #리엘 : 지하에는 리나가 혼자 있다고! 지하로 내려가야 해.
 ch_Riel "Lina is there alone!! We have to go there."

 #우리의 언성이 높아지자, 오스카가 이를 말렸다.
 "Oscar intervened to stop our argument."

 hide Riel with dissolve
 hide Trey with dissolve

 show Oscar a angry at left with dissolve

 #오스카 : 다들 조용히 좀 해. 빨리 들어오라고, 부추기는 것도 아니고.
 ch_Oscar "Be quiet everyone. Just get in here, for crying out loud."

 show Teacher a angry at right with dissolve

 #담임 선생님 : 내가 여기를 막고 있을 테니, 너희들은 얼른 내려가서 리나를 구하고 밤을 끝 낼 방도를 찾아라.
 ch_Teacher "I will stop that monster, go ahead and find a way to save Lina and all of us."

 hide Oscar with dissolve
 show Riel a solid at left with dissolve

 #리엘 : 하지만.
 ch_Riel "But..."

 show Teacher a smile at right

 #담임 선생님 : (웃으며) 난 죗값을 치러야지.
 ch_Teacher "I have to pay for what I did."

 hide Riel with dissolve

 show Jane a sad at left with dissolve

 #제인 : (눈물이 고인 채) 선생님...
 ch_Jane "Teacher ..."

 hide Jane with dissolve

 show Oscar a angry at left with dissolve

 #오스카 : 이럴 시간도 없어. 어서 서둘러.
 ch_Oscar "We haven't got the time for this. Hurry up."

 hide Oscar with dissolve

 show Riel a smile at left with dissolve

 #리엘 : 선생님, 금방 갔다 올게요. 무사하셔야 해요.
 ch_Riel "Teacher, we will be back soon. Please stay safe."

 show Teacher a idle at right

 #담임 선생님 : 너희들도 무사해라.
 ch_Teacher "You guys too."

 hide Riel with dissolve
 hide Teacher with dissolve

 #우리는 문을 열고, 한 명씩 들어가기 시작했다.
 "We opened the door and began to enter one by one."

 show Riel a idle at left with dissolve

 #리엘 : 트레이. 안 들어와?
 ch_Riel "Trey. Aren't you coming in?"

 show Trey a smile at right with dissolve

 #트레이 : 난 남아서, 담임 선생님을 돕다가 들어갈게. 난 반장이잖아.
 ch_Trey "I'll stay here and help our teacher. I'm the class rep after all."

 show Riel a solid at left

 #리엘 : ...알았어. 조심해서 들어와야 해.
 ch_Riel "...All right. Please be careful."

 hide Riel with dissolve
 hide Trey with dissolve

 #트레이와 담임 선생님을 내버려 둔 채, 우리는 지하로 내려가기 시작했다. 모두가 안전하기를 기도하며...
 "Leaving Trey and the homeroom teacher behind, we headed to the basement. I hope everyone is safe..."

 scene black with fade

 #리엘 : 이제 리나를 구할 시간이야.
 ch_Riel "It's time to save Lina."

 stop music


 #S#28. INT. 지하 / 밤

 play music "bgm/5.mp3"

 #그 문은 지하로 내려가는 문이었다.
 "That door lead us to the basement."

 #작은 불빛에 의지하여 사다리를 타고 내려왔다.
 "I relied on the small light to came down the ladder."

 scene pl32 with fade


 show Oscar a idle at left with dissolve
 show Jane a sad at right with dissolve

 #제인 : 어두워... 그리고 냄새...
 ch_Jane "It's dark ... And stinks..."

 #제인은 자신의 코를 잡았다. 역한 냄새가 코를 찌른다. 시체 썩는 냄새가 진동을 한다.
 "Jane grabbed her nose. The foul stench hit us. It is the stench of corpses rotting."

 show Oscar a solid at left

 #오스카 : 욱..
 ch_Oscar "Wook .."

 #지하실은 어둡고 축축하다.
 "The basement is dark and wet."

 #우린 어둠에 익숙해질 때까지 냄새의 존재를 알지 못한 채, 가만히 기다릴 수밖에 없었다.
 "We couldn't do anything but wait, until we got used to the darkness and figured out where the smell came from."

 show Jane a surp at right

 #제인 : (놀래서) 꺄악!
 ch_Jane "Kiyaaa!"

 hide Oscar with dissolve
 hide Jane with dissolve

 show il45 with fade

 #어둠에 익숙해지니 보이는 것 어딘가 제대로 성한 곳 없이 버려진 시체들이다. 제인은 외마디 비명소리를 내며 주저앉아버렸다.
 "After being accustomed to the darkness, we saw mutilated body parts. Jane screamed and collapsed."

 #오스카 :　이건...
 ch_Oscar "They are.."

 #리엘 : 우리 반 아이들이잖아..!
 ch_Riel "They're our classmates....!"

 #실종되었던 아이들의 시체들이 다 여기에 있었다니...
 "The bodies of the missing students were all here ..."

 #리엘 : 하지만 케이는 어디에...
 ch_Riel "But where is Kei ..."

 #하지만 마지막 희생자인 케이가 보이지 않는다.
 "However, the last victim, Kei, is missing."

 #제인은 몸서리를 치면 앞장 서 갔다.
 "Jane, while shivering in fear, lead the way."

 #제인 : 더 들어가 보자. 여기에 있기 싫어!
 ch_Jane "Let's go inside. I do not want to be here any longer!"

 #S#29. INT. 지하 깊숙한 곳 / 밤

 scene pl33 with fade

 #지하 깊숙이 들어가자, 문이 하나가 보인다.
 "We found a door deep inside the basement."

 show Oscar a solid at left with dissolve

 #오스카 : 웬 지하에 방이?
 ch_Oscar "Why is there a room in the basement?"

 show Riel a solid at right with dissolve

 #리엘 : 들어가 보자.
 ch_Riel "Let's go inside."

 hide Oscar with dissolve
 hide Riel with dissolve

 #(S) 문 열리는 소리
 play sound "sfx/8.mp3"
 scene pl34 with fade

 #리엘 : 으...여긴 뭐지?
 ch_Riel "Uh ...What is this place?"

 #내가 앞장 서, 문을 열고 들어갔다. 그때.
 "I took the lead and opened the door. However..."

 scene pl33 with fade

 #(S) 문 닫히는 소리
 play sound "sfx/10.mp3"

 #리엘 : 어?
 ch_Riel "Huh?"

 #내가 들어오는 순간 문이 닫혀버렸다. 어쩔 수 없이, 제인과 오스카는 밖에서 기다리기로 했다.
 "The moment I came in, the door closed. Inevitably, Jane and Oscar had to wait outside."

 scene pl34 with fade

 show Riel a idle at center with dissolve

 #리엘 : 실험실인가? 좀 이상한데.
 ch_Riel "Is it a laboratory? It's a bit weird."

 #마치 실험실로 보이는 공간이다.
 "It is a room seemed like a laboratory."

 #가장 독특한 점은 모든 물건이 붉게 물들어져 있는 것이다. 아마...피인 것 같다... 게다가 옆에는 장기가 담겨 있는 유리병이 가득이다.
 "One weird thing was that everything here was covered in red. It seems..It seems to be blood ... Moreover, the room is filled with jars that contain body organs."

 show Riel a terra at center

 #리엘 : 으...
 ch_Riel "Ew.."

 #리엘은 그 징그러움에 인상을 찌푸렸다.
 "Riel frowned upon the disturbing view."

 #??? : 읍읍..
 ch_unknown "...!!"

 show Riel a surp at center

 #리엘 : ?? 뭐지?
 ch_Riel "??? What was that?"

 #어디선가 소리가 들린다.
 "I hear a sound somewhere."

 #난 소리의 찾아, 안쪽으로 들어왔다.
 "Following the sound, I went deeper in the room."

 #리엘 : 감옥인가? 웬 감옥...
 ch_Riel "Is it a prison? Why is there a prison.."

 #....!! 리나!!
 ".... !! Lina!!"

 hide Riel with dissolve

 #리나는 안대를 쓰고, 입까지 막힌 상태로 감옥에 갇혀 있다.
 "Lina was locked in the jail, with an eye pad and a gag."

 #열어줘야 하는데... 하지만 문이 잠겨 있다. 아마 어떤 장치를 열어 야지 풀어 날 수 있는 것 같다. 방에서 그 열쇠를 찾아보자.
 "I have to free her... But the door is locked. It seems like you have to unlock a lock device to open it. Let's find a key in the room."

 stop music



 menu:
    "Open the drawer.":
      jump drawer
    "Open the big pot.":
      jump pot

 return

 #30_1 서랍을 열어본다.
 #30_2 큰 항아리를 열어본다.


label drawer:

 play music "bgm/10.mp3"

 #S#30_1. INT. 지하 깊은 곳 / 밤

 show il46 with fade

 #굉장히 낡아 보이는 서랍이 있다.
 "There is a drawer that looks very old."

 #리엘 : 으 먼지.
 ch_Riel "It's dusty."

 show il47 with fade

 #서랍을 여니, 먼지가 날린다.
 "Dust blew everywhere as I opened the drawer."

 #리엘 : 콜록콜록. 이게 다 뭐야. 뭔 종이가.
 ch_Riel "Cough cough.. What's all this? Why is there a paper?"

 #...?
 "...?"

 #XX연구소 대표. 만길.
 "XX Institute representative. Gil, Man."

 #리엘 : 교장선생님의 이름이잖아?
 ch_Riel "Isn't that the principal's name?"

 #그 안에는.... 지금까지 교장선생님의 만행이 나와 있다. Y그룹과의 횡령 교직원 폭행사건 그리고 살인까지...
 "Inside it .... there are records of the principal's wrongdoings. Embezzlement from Y Group, physical abuse of faculty and even murder..."

 jump c1


 return


label pot:

 play music "bgm/10.mp3"


 #S#30_2. INT. 지하 깊은 곳 / 밤

 show il48 with fade

 #리엘 : 웬 항아리가?
 ch_Riel "Why is there a pot here?"

 #이곳과 어울리지 않는 항아리다. 한 번..열어볼까?
 "The pot kind of seemed out of place. Let's see..Should I open it?"

 show il49 with fade

 $ achievement.grant("Kei")
 $ achievement.Sync()


 #리엘 : !!!
 ch_Riel "!!!"

 #케이... 케이의 시체가 왜 여기에!!
 "Kei... Why is Kei's body here !!"

 #얼굴을 뺀 모든 부분에 난도질이 되어있다. 케이도 교장선생님의 희생양..?
 "Every part of his body except the face was mangled horribly. Was Kei another victim of the principal's plan..?"

 #리엘 : ...응? 케이는 교장선생님의 아들인데. 왜 자기 아들을...! 게다가 원한이 있는 것 마냥 난도질을..대체.
 ch_Riel "...Huh? Kei is the son of the principal. Why would he kill his son ...! Why would he do such a horrible thing to his son...Just why.."

 jump c1


 return


label c1:

 #(S) 제인의 비명소리


 #!!밖에서 비명소리가 난다.
 "!!Somebody screamed outside."



 #S#31. INT. 지하 깊은 곳 / 밤

 scene pl35 with fade

 #제인의 비명소리다. 급하게 방을 나갔다. 다행히도 안에서 잠기는 구조였는지, 쉽게 열린다.
 "It's Jane's scream. I left the room hastily. Luckily, the door opens from inside."

 scene pl36 with fade

 show Riel a surp at center with dissolve

 #리엘 : 트레이! 거기서 뭐하는 거야!
 ch_Riel "Trey! What are you doing there ?!"

 hide Riel with dissolve

 show il50 with fade

 #트레이는 제인의 목을 잡고 칼로 위협하고 있다.
 "Trey grabbed Jane's neck and threatens her with a knife."

 $ achievement.grant("Traitor")
 $ achievement.Sync()


 #리엘 : 오스카! 트레이가 왜!
 ch_Riel "Oscar! What's Trey doing?!"

 #오스카 : ...제인이 위험해. 미친 자식.
 ch_Oscar "...Jane is in danger. Crazy bastard."

 #트레이 : 그래, 내가 미친 거일수도 있겠지. 하지만 내 상황이 된다면 다들 안 미칠 수가 없을 걸?
 ch_Trey "Yeah, I might be crazy. But who wouldn't turn crazy in the situation that I'm in?"

 #리엘 : 뭐?
 ch_Riel "What?"

 #트레이 : 너희들은 이기적이야.
 ch_Trey "You guys are selfish."

 #오스카 : 저 자식 또 시작이네.
 ch_Oscar "There he goes again."

 #리엘 : 대체 뭔 소리는 하는 거야?
 ch_Riel "What the hell are you talking about?"

 #트레이 : 너넨 이 밤이 끝나야 살 수 있겠지만, 나는...난 사라지고 말 거야. 난 평생 이 밤을 지속시켜서, 이곳에서 군림할 거라고! 근데 왜 자꾸 너희가 방해해!
 ch_Trey "You can live on after the night ends, but I ...I will banish. I won't let this night end, and I will reign here forever! Stop ruining my plan!"

 #리엘 : 그렇다면 넌 모든 걸 알고...
 ch_Riel "Then you knew everything ..."

 #트레이 : 그래, 맞아. 교장선생님이 다 저지른 일이지. 교장선생님이 XX그룹의 대표인 거 다 알고 있잖아? 난 그런 상태로 죽고 싶지 않았 단 말이야. 난 평생 여기에 살아있을 거야!
 ch_Trey "Yeah. The principal is behind all of this. You all know that the principal was the president of XX Group! I don't want to die. I will live here forever!"

 #리엘 : ...담임 선생님은...설마?
 ch_Riel "…The HR teacher..Could he be?"

 #트레이 : 지금쯤이면 신나게 먹히고 있겠군.
 ch_Trey "By now, he's probably being eaten mercilessly."

 #오스카 : 나쁜 자식...
 ch_Oscar "You bastard ..."

 #리엘 : 이건 모두에게 좋지 않아. 그만 둬. 네가 그렇게 된 건 안타깝지만...
 ch_Riel "This is not good for everyone. Please stop. It's a shame you ended up that way..."

 #트레이 : 내가 진정 안타깝다면, 당장 그 방에서 나와. 이건 권유가 아니라 협박이야. 이 밤을 끝내는 것을 포기한다면, 이 아이를 살려주지.
 ch_Trey "If you really feel sorry for me, get out of that room at once. This is an order, not a request. If you give up about ending this night, I'll let this girl go."

 #트레이는 정말 제인을 찌를 것만 같이 위협하고 있다. 어떻게 해야 하지...
 "Trey seems like he's really going to stab Jane. What should I do..."



 menu:
    "Try to talk it out.":
      jump talk
    "Enter the room and lock the door.":
      jump lock

 return

 #32_1 대화를 시도한다.
 #32_2 방에 들어가서 문을 잠근다.


label talk:


 #S#32_1

 #리엘 :　다시 한 번 생각해봐.
 ch_Riel "You don't have to do this."

 #트레이 : (비웃는다) 빨리 결정을 내리는 것이 좋을 걸.
 ch_Trey "You better make a quick decision."

 #트레이를 설득하려고 했지만, 이는 통하지 않을 듯싶다.
 "I tried to change Trey's mind, but it did not seem to work."

 #...그때 뒤에서 붉은색 그림자가 다가오기 시작한다.
 "...The red shadow started to come from behind."

 #메두사잖아... 메두사가 반가웠던 건 이번이 처음이다.
 "It's the Medusa ...This is the first time it felt food that the Medusa was coming."

 #오스카 : ...
 ch_Oscar "..."

 #오스카와 눈이 마주쳤다. 우리는 뜻이 통한 마냥 고개를 끄덕였다.
 "Oscar and I looked into each other's eyes. We nodded as if we agreed on something."

 #오스카 : 어 트레이. 저기 뒤에 담임 선생님 아닌가? 오스카의 어색한 목소리에 난 고개를 저었다. 저걸 속을 리가...응?
 ch_Oscar "Hey Trey. Isn't that our teacher behind you? The awkward voice of Oscar made me cringe. What kind of idiot would fall for that.. Huh?"

 #트레이 : 뭐? 분명 죽었을 텐...으악!
 ch_Trey "What? But how! He should be dead...Ahh!"

 show il51 with fade

 #오스카의 말을 듣고 트레이는 뒤를 돌아봤다.
 "Trey looked back after hearing what Oscar said. "

 #리엘 : 제인, 오스카! 빨리 이 안으로 들어와!! (33)
 ch_Riel "Jane, Oscar! Get in here quickly!"

 stop music


 jump jin

 return

label lock:


 #S#32_2.
 #트레이 말을 들어주면, 리나는 누가 구해주지? 그러다간 결국 우리는 다 죽게 될 거야... 아이들한테는 미안하지만, 리나가 더 소중해. 그리고 이 밤은 끝나야 한다고!
 "If we do as Trey says, who will save Lina? We are all going to die... I'm sorry for the other kids, but Lina is lot more important to me. And this night must be ended!"

 #제인 : 리엘!
 ch_Jane "Riel!"

 #트레이 : 이 자식이!
 ch_Trey "You bastard!"

 scene pl36 with fade

 #나는 서둘러 방 안으로 들어와, 문을 닫았다. 밖에서 비명소리가 들린다.
 "I ran into the room and closed the door. I heard a scream outside."

 #(S) 비명소리.


 #리엘 : ......
 ch_Riel "......"

 #비명소리가 줄어들고, 밖은 소름끼칠 정도로 조용하다.
 "The screams started to cease, and it's awfully quiet outside.."

 #리엘 : ....
 ch_Riel "...."

 #문을 닫자, 그 옆 빨간 버튼이 눈에 보인다.
 "As I close the door, I see a red button beside it."

 #리엘 : 아깐 제대로 못 봤나보군...
 ch_Riel "Oh, must have missed it before..."

 stop music

 menu:
    "Press.":
      jump press
 return

label press:


 #36_ 누른다.


 #S#36. INT. 지하 방 / 밤
 #(진동/리엘, 배경 흔들림)

 play music "bgm/2.mp3"
 scene pl35 with fade

 #갑자기 지하가 울리기 시작한다. 가만히 버티고 서있을 수 없어, 문고리를 붙잡았다. 점점 진동이 잦아든다.
 "Suddenly the ground's shaking. I couldn't stand on my own, so I hold the door knob. Gradually, the shaking started to stop."

 #리엘 : 리나!
 ch_Riel "Lina!"

 #진동이 완전히 멈추자, 잠겨 있던 철창이 열렸다. 난 조심스럽게 리나를 부축해서 방문을 열었다. 방문을 열자...
 "When the shaking stopped completely, the locked iron bars opened. I carefully helped Lina to move and opened the door. When I opened the door..."

 show il52 with fade

 #바닥에는 피로 물든 채 쓰러져 있는 제인, 오스카가 보인다.
 "all I could see was Jane and Oscar who were lying down covered in blood."

 #......
 "......"

 #…
 "...."

 #..
 ".."

 #.
 "."

 show il53 with fade

 #이제 밖에서는 해가 뜨고 있는 것 같다. 모든 것이 끝났다.
 "It seems that the sun is rising outside. Everything is over."


 $ achievement.grant("Summer Nightmare")
 $ achievement.Sync()



 #S#37.


 #(흑백배경)
 scene black with fade


 #리엘 : 모든 것이 끝나고, 학교는 원래 상태대로 들어왔다. 오스카와 제인의 빈자리만 빼고. 내가 지하실에서 찾은 자료로 교장선생님은 지금 경찰에 조사를 받고 있다. 아마 이제 거기에 내가 더 이상 참여할 바가 아니겠지. ...그 날 모든 걸 본 리나는, 충격을 받고 정신병원에 입 원했다.
 ch_Riel "After everything ended, life at the school came back to normal."
 ch_Riel "Except for Oscar and Jane. The principal is being investigated by the police with the data I found in the basement."
 ch_Riel "None of that is my business anymore..Unfortunately, Lina, who witnessed everything, is hospitalized due to shock and stress."

 #난... 내 친구들은 다 죽었지만, 난 살아남았다. 그게 최선이었다고 믿을 뿐, 난 죄책감을 느끼지 않는다.
 "I... My friends are all dead, but I survived. I did what I could do, and I don't feel guilty about it."

 #...
 "..."

 #..
 ".."

 #내가 연쇄살인의 살인자로 오해 받았었지... 사실 그것이 맞았을 지도 모르겠다.
 "People thought I was the serial killer. Perhaps they weren't wrong after all.."

 stop music

 #▶배드 엔딩3 <비어있는 자리>


 return



label jin:

 #S#33 INT. 지하 방 / 밤
 play music "bgm/9.mp3"
 scene pl38 with fade

 #오스카와 제인을 붙잡고 방에 들어오는 것에 성공했다. 나는 서둘러 문을 닫았다.
 "I successfully entered the room with Jane and Oscar. I hurried and closed the door."

 #(S) 문이 잠기는 소리.
 play sound "sfx/12.mp3"

 #밖에서는 트레이의 비명소리가 들리는 것 같다. 메두사가 여기까지 들어오기 전에, 이 밤을 끝내고 리나를 구해야 해.
 "Trey seems to be screaming outside. Before Medusa gets here, we have to end everything and save Lina."

 show Jane a surp at right with dissolve

 #제인 : 여기 침대에..!
 ch_Jane "Look at the bed!"

 hide Jane with dissolve

 show il54 with fade

 #방의 중앙에는 침대가 있다. 침대 위에는 여자로 추정되는 것이 누워있다.
 "There is a bed in the center of the room. On the bed, there was a body of a woman."

 #오스카 : 메두사 실험의 실험체였나 봐...
 ch_Oscar "she must have been one of the victims of the Medusa experiment..."

 #제인 : 너무 안타까워...
 ch_Jane "What a tragedy..."

 #침대위의 여자의 얼굴은 함몰되어 있어서 알아 볼 수가 없다.
 "The face of the woman was demolished to the point it was impossible to identify."

 #제인 : 우리 얼굴을 덮어주자.
 ch_Jane "Let's cover her face."

 #리엘 : ...응.
 ch_Riel "…yeah."

 show il55 with fade

 #제인의 제안에 여자의 얼굴을 흰 천으로 덮었다.
 "Oscar took Jane's suggestion and covered the woman's face with a white cloth."

 #오스카 : 좋은 곳으로 갔기를..
 ch_Oscar "Rest in piece..."

 #제인 : 위에서는 행복하세요.
 ch_Jane "Hope you're in a better place."

 #리엘 : ...(눈을 감는다.)
 ch_Riel "..."

 # (진동/인물, 배경 흔들림)
 scene pl38 with hpunch


 #갑자기 지하가 울리기 시작한다.
 "Suddenly the ground started to shake"

 #가만히 버티고 서있을 수 없어, 문고리를 붙잡았다. 점점 진동이 잦아든다.
 "I could not stand on my own, I grabbed the door knob. The shaking started to cease."

 #리엘 : 리나!
 ch_Riel "Lina!"

 #진동이 완전히 멈추자, 잠겨 있던 철창이 열려 있다. 난 조심스럽게 리나를 부축해서 아이들과 함께 문을 열었다.
 "The shaking stopped completely, and the locked door opens. I helped Lina move carefully, and opened the door with other students. "

 show il53 with fade

 #제인 : 빛이 들어오고 있어!
 ch_Jane "The light is coming in!"

 #오스카 : 이제 밤이 끝났어.
 ch_Oscar "The night is over."

 #아침이 오고 있다...모든 게 끝났다.
 "The morning is coming...Everything is over."

 #(암전)
 scene black with fade
 stop music


 #S#34. EXT. 리엘의 집 앞 / 아침
 play music "bgm/11.mp3"
 scene pl39 with fade

 show Riel b idle at left with dissolve
 show Lina b smile at right with dissolve

 #리나 : 빨리 와. 리엘! 이러다가 지각하겠어.
 ch_Lina "Come on, Riel! We'll be late at this rate."

 show Riel b smile at left

 #리엘 : ...(미소)
 ch_Riel "..."

 hide Riel with dissolve
 hide Lina with dissolve

 #(리엘이 리나의 손을 잡는 것 클로즈업)
 scene il56 with fade
 "..."


 #S#35. INT. 학교 / 오전

 scene pl40 with fade
 show Student1 b idle at left with dissolve
 #학생1 : 리엘 안녕?
 ch_Student1 "Riel, how are you?"
 show Student2 b idle at right with dissolve
 #학생2 : 또 둘이 같이 다니네. 이제 진짜 사귀는 거냐?
 ch_Student2 "You guys are always together. Are you really dating now?"
 hide Student2 with dissolve
 show Lina b shy at right with dissolve

 #리나 : (얼굴을 붉히며) 그런 말 하지 마!
 ch_Lina "Don't say that!"
 hide Student1 with dissolve
 show Jane b smile at left with dissolve

 #제인 : 리나야, 얼른 반에 가자.
 ch_Jane "Lina, let's go to class."

 hide Jane with dissolve
 show Oscar b solid at left with dissolve

 #오스카 : 너희 복도에서 시끄럽게 굴지 말고, 얼른 교실 안으로 들어가.
 ch_Oscar "Don't make noise in the hallway and go into the classroom straight away."

 hide Oscar with dissolve
 hide Lina with dissolve

 #(백색 배경)
 scene black with fade

 #리엘 : 이 밤이 끝나고, 학교는 모두 제자리로 들어갔다. 교장 선생님은 내가 지하에서 찾은 자료들을 증거로, 지금 경찰에서 조사를 받고 있다. 담임 선생님은... 그 날 돌아가셨지만, 모 두들 담임 선생님을 존경하며 추모하고 있다. 아무튼 이제 모든 것이 정리가 되었고, 밝혀졌 다. 이제 나도 일상으로 돌아가야지. ....근데 교장 선생님은 정말 자신의 아들까지 죽인 것일 까? ...
 ch_Riel "After the night ended, everything went back into place."
 ch_Riel "The principal is being investigated by the police with the evidence that I found in the basement."
 ch_Riel "Our HR teacher... He passed away that day, and everyone in the school commemorates him with respect. Everything's revealed and resolved."
 ch_Riel "Now I must go back to my life too. ....I wonder though.. Did the principal go so far to kill his own son?"

 stop music

 #▶노멀 엔딩 <밝혀지지 않은 진실>

 return
