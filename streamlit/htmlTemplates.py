css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #d2d6e2
}
.chat-message.bot {
    background-color: #d4d8e4
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
.block-container{
    max-width: 70rem;
}
body {
    max-width: 2200px;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
[data-testid="stAppViewContainer"]{
    background-image: url('https://img.freepik.com/vecteurs-libre/concept-transformation-numerique-vecteur-fond-cerveau-technologie-ia_53876-117820.jpg?w=2000');
    background-size: cover;
}
[data-testid="stHeader"]{
     display: none;
}
span.css-10trblm.e16nr0p30{
    text-align: center;
    margin-bottom:70px;
}


.css-12ttj6m.epcbefy1 {
    margin-top: 30px;
}

.css-12ttj6m{
    border: none;
}

.css-184tjsw p {
      font-size: 20px;
}

.element-container.css-kxz5b8.e1tzin5v3 {
        margin-left: -15px;
        
}

section.css-po3vlj.exg6vvm15 {
        width: 1060px;
}
textarea.st-bf.st-c0.st-c1.st-c2.st-c3.st-c4.st-c5.st-c6.st-c7.st-c8.st-c9.st-b8.st-ca.st-cb.st-cc.st-cd.st-ce.st-cf.st-cg.st-ch.st-ae.st-af.st-ag.st-ci.st-ai.st-aj.st-bz.st-cj.st-ck.st-cl.st-cm.st-cn.st-co {
    min-height: 200px;
}

.chat-message .message {
    color: #303030;
}

button.css-1x8cf1d.edgvbvh5{
    background-color: #d4d8e4;
    border-radius: 0px;
}

button.css-1x8cf1d.edgvbvh5:hover{
    border-color: #d4d8e4;
    color: #000000;
}

button.css-1x8cf1d.edgvbvh5:active{
    border-color: #d4d8e4;
    color: #000000;
}

.css-1offfwp p {
    font-size: 20px;
}

button.css-1x8cf1d.edgvbvh10{
    background-color: #d4d8e4;
    border-radius: 0px;
}

'''
bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://saffroninteractive.com/wp-content/uploads/2018/09/saffbot_temp_transparent.png" style="max-height: 100px; max-width: 40px;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''
user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://us.123rf.com/450wm/blankstock/blankstock1605/blankstock160502581/56305912-speech-bubbles-icon-chat-or-blogging-sign-communication-symbol-orange-circle-button-with-icon-vector.jpg?ver=6" style="max-height: 40px; max-width: 40px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''