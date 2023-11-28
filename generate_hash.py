import streamlit_authenticator as stauth
hashed_passwords = stauth.Hasher(['password1', 'password2']).generate()
print(hashed_passwords)