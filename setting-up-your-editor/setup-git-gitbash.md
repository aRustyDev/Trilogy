# Setting Up Git
<img src="./img/git-bash-img.png" alt="Atom" width="75"/>

## Install Git & GitBash
1. Go to https://git-scm.com/
1. Click *Download for OS*
1. Run the Downloaded file
1. Destination location should be `C:\Program Files\Git`
1. Click Next
1. Select your Default Editor to use as Gits default editor
1. Click next
1. Click next (use recommended)
1. Use the OpenSSL Library
1. Checkout Windows-style, commit Unix-style line endings 
1. Use MinTTY 
1. Default (fast-forward or merge). 
1. Git Credential Manager Core
1. Use default, click next
1. Click install
1. Finish

### Create GPG Key 
1. `gpg --default-new-key-algo rsa4096 --gen-key`  
2. `gpg --list-secret-keys --keyid-format=long`  
3. `gpg --armor --export <KeyID-FromAboveCmd>`  
4. Then just Copy your GPG key, beginning with `-----BEGIN PGP PUBLIC KEY BLOCK-----` and ending with `-----END PGP PUBLIC KEY BLOCK-----`  

### Create Personal Access Token
1. Go to your [**GitLab** - Profile/AccessTokens](https://umn.bootcampcontent.com/profile/personal_access_tokens)
1. Add a name
1. Set Expiration (if you want, its not required)
1. Give it *read_user*, *read_repository*, & *write_repository* scopes.
1. Click 'Create personal access token'
1. Copy the Token (it will not be shown again, so save it somewhere safe.)

**NOTE**: its not critical to keep this token, its very easy to just recreate a new one. But its good practice to handle it with care. 
