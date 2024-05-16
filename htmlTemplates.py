css = '''
<style>
@keyframes float {
    0% {
        transform: translateY(0px);
    }
    50% {
        transform: translateY(-20px);
    }
    100% {
        transform: translateY(0px);
    }
}

.wizard-hat {
    animation: float 3s ease-in-out infinite;
}
body {
    background-image: url('https://images.unsplash.com/photo-1618944913480-b67ee16d7b77?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'); /* Ensure this is a valid URL */
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    font-family: 'Roboto', sans-serif;
    background-color: transparent !important;
}

html{
background-color: transparent !important;
}
.stApp {
    background-image: url('https://images.unsplash.com/photo-1618944913480-b67ee16d7b77?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'); /* Ensure this is a valid URL */

    background-color: "#FCCD12; /* Make sure the app background is transparent to show the image */
}

#root {
 background-color: transparent !important;
}

header {
    background-color: transparent !important;
}

/* Remove background from the footer */
[data-testid="stFooter"] {
    background: transparent !important;
}
.st-emotion-cache-1dp5vir:last-of-type {
    background: transparent !important;
}

/* Additional styles to target the potential children of the footer div to ensure transparency */
.st-emotion-cache-1dp5vir:last-of-type div {
    background: transparent !important;
}

/* Typography */
 h1, h2, h3, h4, h5, h6 p{
     font-family: 'Pirata One', cursive;
     color: #d4af37;
     text-shadow: 2px 2px 4px #000000;
}

.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
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

header, .st-footer {
    background-color: transparent;
}
/* Remove the Streamlit hamburger menu background - optional */
.css-1v3fvcr {
    background-color: transparent;
}

/* Remove Streamlit branding background - optional */
.css-1y0tads {
    background-color: transparent;
}

/* Remove background and border from main content area */
.stApp > div {
    background-color: transparent;
    border: none;
}

/* Make full app background transparent */
body {
    background-color: transparent;
}
@import url('https://fonts.googleapis.com/css2?family=Pirata+One&display=swap');
</style>

'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMcQvmKkUVgmobOXtFbSrxj8V6g6TlPY_FhINWExOpoknF3IaODMR2F-pcAh8jaHo9CkU&usqp=CAU" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://static.vecteezy.com/system/resources/previews/004/607/791/large_2x/man-face-emotive-icon-smiling-male-character-in-blue-shirt-flat-illustration-isolated-on-white-happy-human-psychological-portrait-positive-emotions-user-avatar-for-app-web-design-vector.jpg" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;"">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''

