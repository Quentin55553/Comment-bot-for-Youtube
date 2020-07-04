################################
####Made by Novritch - GitHub###
# quentin.fillion.95@outlook.fr #
#################################
# Requirements to run this script correctly :
#    - Work with Microsoft Edge (if it's another brower you can change it line 20, ex : webdriver.firefox(), webdriver.chrome(), webdriver.ie()...)
#    - WebDriver for your Browser (here Edge)
#    - Selenium module
# Once this script started, all your current tabs on the selected brower will be automatically closed, be careful !
# This script work unically with YouTube playlist links
# This script was realized with my loadings times, so you can change lines with time.sleep(x) as your please to increase the speed, if your browser and connection allow it

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def PosterCommentaire(commentaire,playlist):
    driver = webdriver.Edge()
    driver.get(playlist)
    driver.maximize_window()
    try:
        myElem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'thumbnail')))
        print ("Playlist's content loaded successfully !")
        elementParent = driver.find_element_by_xpath("//div[(@id='contents') and (@class = 'style-scope ytd-playlist-video-list-renderer')]")
        nombreDeVideos = len(elementParent.find_elements_by_xpath("//ytd-playlist-video-renderer[(@class = 'style-scope ytd-playlist-video-list-renderer')]"))
        driver.find_element_by_id('thumbnail').click()
        for i in range(nombreDeVideos):
            time.sleep(10)
            # Ecriture commentaire
            driver.execute_script("window.scrollTo(0, 750)")
            time.sleep(3)
            driver.find_element_by_id('placeholder-area').click()
            inputBox = driver.find_element_by_id('contenteditable-root')
            inputBox.send_keys(commentaire)
            driver.find_element_by_id('submit-button').click()
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, -750)")
            driver.find_element_by_xpath("//a[(@class='ytp-next-button ytp-button')]").click()
        print("Process completed !")
    except TimeoutException:
        print ("The PlayList takes too long to load (<20 seconds) or there is a problem studying the Web page")


# Connexion au compte Google
def ConnexionGoogle(email,MDP):
    driver = webdriver.Edge()
    driver.get("https://accounts.google.com/signin/oauth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3ABBC%2C16%3A59aa2292b79a6ba4%2C10%3A1593795256%2C16%3A5340420ffe98a9f0%2C26978fbbeb4f365b1c584b05ac01158b1379fd0eb20732ec7437658da0cc3e36%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%2265784dfa8081468fb90a9fc123c46818%22%7D&response_type=code&o2v=1&as=uIUgZGCNL2eXi6vXPoq9WQ&flowName=GeneralOAuthFlow")
    time.sleep(1)
    driver.find_element_by_name('identifier').send_keys(email)
    driver.find_element_by_id('identifierNext').click()
    time.sleep(1)
    driver.find_element_by_name('password').send_keys(MDP)
    time.sleep(1)
    driver.find_element_by_id('passwordNext').click()
    time.sleep(1)
    driver.close()
    PosterCommentaire(commentaire,playlist)

# Dialogue avec l'utilisateur
reponse = input(str("Is your Google account currently connected ? (yes OR no)")) #There must not be a single account saved in your brower, delete all, otherwise it wouldn't work
if reponse == "no":
    email = input(str("Enter your Google account email"))
    MDP = input(str("Enter your Google account password"))
    playlist = input(str("Enter the link of the playlist containing the videos under which to put the comments (ex : https://www.youtube.com/playlist?list=SPECIFICID)"))
    commentaire = input(str("Enter the comment that you want to post"))
    ConnexionGoogle(email,MDP)
if reponse == "yes":
    playlist = input(str("Enter the link of the playlist containing the videos under which to put the comments (ex : https://www.youtube.com/playlist?list=SPECIFICID)"))
    commentaire = input(str("Enter the comment that you want to post"))
    PosterCommentaire(commentaire,playlist)