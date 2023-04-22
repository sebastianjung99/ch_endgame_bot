import pyautogui
import time
import re
import itertools
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

from multiprocessing.pool import ThreadPool



amount_ACs = 14
amount_quests = 40

coords = {
    'options'           :       {'left' : 2453  ,   'top' : 72      },
    'save'              :       {'left' : 797   ,   'top' : 376     },
    'import'            :       {'left' : 797   ,   'top' : 487     },
    'import_confirm'    :       {'left' : 1278  ,   'top' : 1122    },
    'import_exit'       :       {'left' : 2067  ,   'top' : 190     },
    'exit_options'      :       {'left' : 1984  ,   'top' : 280     },

    'ascend'            :       {'left' : 2461  ,   'top' : 553     },
    'ascend_confirm'    :       {'left' : 1103  ,   'top' : 1048    },
    'level_low'         :       {'left' : 258   ,   'top' : 546     },
    'scroll_top'        :       {'left' : 1237  ,   'top' : 469     },
    'scroll_bottom'     :       {'left' : 1236  ,   'top' : 1320    },
    
    'shop'              :       {'left' : 1904  ,   'top' : 1317    },
    'timelapses'        :       {'left' : 609   ,   'top' : 782     },
    'timelapse_8'       :       {'left' : 1596  ,   'top' : 462     },
    'timelapse_24'      :       {'left' : 1596  ,   'top' : 696     },
    'timelapse_48'      :       {'left' : 1596  ,   'top' : 948     },
    'timelapse_168'     :       {'left' : 1596  ,   'top' : 1182    },
    'timelapse_confirm' :       {'left' : 1113  ,   'top' : 881     },
    'timelapse_close'   :       {'left' : 1914  ,   'top' : 119     },
    'shop_close'        :       {'left' : 2406  ,   'top' : 89      },

    # tabs
    'tab_merc'          :       {'left' : 1048  ,   'top' : 242     },
    'tab_heroes'        :       {'left' : 157   ,   'top' : 243     },

    'merc_0'            :       {'left' : 810   ,   'top' : 555     },
    'merc_1'            :       {'left' : 810   ,   'top' : 792     },
    'merc_2'            :       {'left' : 810   ,   'top' : 1032    },
    'merc_3'            :       {'left' : 810   ,   'top' : 1267    },
    # need to scroll before accessing last merc!!
    'merc_4'            :       {'left' : 810   ,   'top' : 1130    },

    'quest_0'           :       {'left' : 1022  ,   'top' : 331     },
    'quest_1'           :       {'left' : 1022  ,   'top' : 596     },
    'quest_2'           :       {'left' : 1022  ,   'top' : 851     },
    'quest_3'           :       {'left' : 1022  ,   'top' : 1045    },    
    'quest_accept'      :       {'left' : 1850  ,   'top' : 761     },

    'auto_clicker_spot' :       {'left' : 1542  ,   'top' : 1246    },

    'gilded_close'      :       {'left' : 2388  ,   'top' : 75      },
    
    # ascend relics pop-up
    'ascend_relic_popup':       {'left' : 1119  ,   'top' : 887     },
}

regions = {
    #                       (x, y,  width, height)
    'left'              :   (5, 189, 1270, 1200),
    'right'             :   (1476, 37, 1100, 1360),
    'skills'            :   (1289, 303, 150, 1080),

    # mercenary Start Quest button
    'merc_0'              :   (593, 500, 500, 130),
    'merc_1'              :   (593, 700, 500, 130),
    'merc_2'              :   (593, 970, 500, 130),
    'merc_3'              :   (593, 1200, 500, 130),
    # need to scroll before the last mercenary
    'merc_4'              :   (593, 1076, 500, 130),    
}

# TODO refactor code to use this dict instead of "hardcoded" links to images, to easily edit them
image_url = r"C:\Users\Sebastian\OneDrive\Dokumente\vscode-workspace\Python\pyautogui\images"
images = {
    # timelapses
    'buy_timelapse'     :   f'{image_url}\\buy_timelapse.png',
    'timelapse_8'       :   f'{image_url}\\timelapse_8.png',
    'timelapse_24'      :   f'{image_url}\\timelapse_24.png',
    'timelapse_48'      :   f'{image_url}\\timelapse_48.png',
    'timelapse_168'     :   f'{image_url}\\timelapse_168.png',
    'timelapse_finished':   f'{image_url}\\timelapse_finished.png',

    # mercenaries
    'merc_collect'      :   f'{image_url}\\merc_collect.png',

    # heroes    
    'maw'               :   f'{image_url}\\heroes\\maw.png',
    'yachiyl'           :   f'{image_url}\\heroes\\yachiyl.png',
    'rose'              :   f'{image_url}\\heroes\\rose.png',
    'sophia'            :   f'{image_url}\\heroes\\sophia.png',
    'blanche'           :   f'{image_url}\\heroes\\blanche.png',
    'dorothy'           :   f'{image_url}\\heroes\\dorothy.png',

    # heroes gild tab    
    'gilded'                 :   f'{image_url}\\misc\\gilded.png',
    'gild_maw'               :   f'{image_url}\\heroes\\gild\\maw.png',
    'gild_yachiyl'           :   f'{image_url}\\heroes\\gild\\yachiyl.png',
    'gild_rose'              :   f'{image_url}\\heroes\\gild\\rose.png',
    'gild_sophia'            :   f'{image_url}\\heroes\\gild\\sophia.png',
    'gild_blanche'           :   f'{image_url}\\heroes\\gild\\blanche.png',
    'gild_dorothy'           :   f'{image_url}\\heroes\\gild\\dorothy.png',

    # gilded heroes    
    'gilded_maw'               :   f'{image_url}\\heroes\\gilded\\maw.png',
    'gilded_yachiyl'           :   f'{image_url}\\heroes\\gilded\\yachiyl.png',
    'gilded_rose'              :   f'{image_url}\\heroes\\gilded\\rose.png',
    'gilded_sophia'            :   f'{image_url}\\heroes\\gilded\\sophia.png',
    'gilded_blanche'           :   f'{image_url}\\heroes\\gilded\\blanche.png',
    'gilded_dorothy'           :   f'{image_url}\\heroes\\gilded\\dorothy.png',

    'buy_upgrades'           :   f'{image_url}\\misc\\buy_upgrades.png',
    
    # ascend relics pop-up
    'ascend_relic_popup':   f'{image_url}\\misc\\relic_popup.png',

    'start_quest'       :   f'{image_url}\\misc\\start_quest.png',
}

save_path = r'C:\Users\Sebastian\OneDrive\Dokumente\clicker_heroes_saves'

short_wait = 0.075
med_wait = 0.2
long_wait = 0.5
extended_wait = 1

chromePath = "C:\Program Files\chromedriver.exe"
edgePath = 'C:\Program Files\msedgedriver.exe'
firefoxPath = 'C:\Program Files\geckodriver.exe'
# driver = webdriver.Firefox(executable_path = firefoxPath)
# driver = webdriver.Chrome(chromePath)

options = Options()
options.add_argument('--window-size=1920,1080')
# supress: INFO = 0, WARNING = 1, LOG_ERROR = 2, LOG_FATAL = 3
options.add_argument('log-level=3')

caps = webdriver.DesiredCapabilities.CHROME.copy()
# none = undefined, eager = page becomes interactive, normal = complete page load
caps['pageLoadStrategy'] = 'eager'

driver_quests = webdriver.Chrome(chromePath, options=options, desired_capabilities=caps)
options.add_argument("--headless")
driver = webdriver.Chrome(chromePath, options=options, desired_capabilities=caps)
# create seperate driver for getting quests so we can do other stuff during it

copying = False

# TODO find out why i can use headless for driver but not for driver_quests, somehow Keys.CONTROL does not work on driver_quests
def manage_mercs(_quest_list, _fast_mode=False):
    """ manages mercs
    _fast_mode: assumes the save file is already in clipboard and ready to be pasted (does not copy the file!)
    """

    if not _fast_mode:
        # copy save file
        copy_savefile('clickerHeroSave_generated.txt')

    driver.get('C:/Users/Sebastian/OneDrive/Dokumente/vscode-workspace/Python/pyautogui/merc_calc/merc_lister_files/saved_resource.html')
    
    try:        
        # wait for page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'savegame')))
        
        # write save game data to textfield
        savegame_box = driver.find_element_by_id('savegame')
        savegame_box.click()
        savegame_box.send_keys(Keys.CONTROL + 'v') 
        global copying
        copying = False       
        
        # driver.save_screenshot('error.png')

        # find import button and click it
        import_button = driver.find_element_by_tag_name('button')
        import_button.click()

        # get lifespan of mercs
        TTD_list = get_merc_status()        
        print('\nget_merc_status')

        # save the indexes from TTD_list of available mercenaries in a list
        available_mercs = []
        for merc_index in range(len(TTD_list)):
            # need to scroll for the last mercenary
            if merc_index == 4:
                # TODO write own function to scroll so we don't forget the sleep after every scroll NotLikeThis
                pyautogui.scroll(-400)
                time.sleep(0.2)
            # append the index of the available mercenary
            if (pyautogui.locateOnScreen(images['start_quest'], grayscale=True, confidence=0.7, region=regions[f'merc_{merc_index}'])) != None:
                available_mercs.append(merc_index)
        
        # scroll to top again
        pyautogui.scroll(400)
        time.sleep(0.2)

        # TODO find out why mcniiby is never chosen but still has 5 hours to live
        # TODO WRITE MORE 'INTELLIGENT' FUNCTION FOR STARTING QUESTS: WATCH ALL QUESTS AND  ASSIGN THEM BASED ON REWARD

        # index of the index of the mercenary (not a typo)
        # available_mercs stores the indexes of the mercs in TDD_list
        # eg. available_mercs = [1, 2, 3] and TDD_list = [2000, 100, 3000, 40000]
        # then TDD_list[available_mercs[2]] == 40000
        merc_index = 0
        # store tries to increment them later if quest start fails, to not get stuck
        tries = 0
        # end when the list is empty (all mercs have quest or are not available) or when tries are exceeded
        while available_mercs and tries < 20 and merc_index < len(available_mercs):
            # start quest if mercenary is not dead
            if TTD_list[merc_index] > 0:                    
                # need to scroll for the last mercenary
                if available_mercs[merc_index] == 4:
                    # TODO write own function to scroll so we don't forget the sleep after every scroll NotLikeThis
                    pyautogui.scroll(-400)
                    time.sleep(0.2)

                # the index of the mercenary to start the quest is stored at available_mercs[merc_index]
                # for more info look at comment above merc_index
                started = start_quest(_quest_list[0], TTD_list, available_mercs[merc_index])
                # if quest was started (started == True) we remove the merc (remove = pop by value) it was started on
                if started:
                    _quest_list.pop(0)
                    available_mercs.remove(available_mercs[merc_index])
                    merc_index = 0
                else:
                    merc_index += 1
                    tries += 1

    finally:
        # driver.close()
        pass

def get_merc_status():
    # find table with data
    alive_div = driver.find_element_by_id('alive')
    table_body = alive_div.find_element_by_tag_name('tbody')
    rows = table_body.find_elements_by_tag_name('tr')

    # Time To Die list
    TTD_list = []

    # save table data
    # start with index 1 as row 0 is used as a header
    for i in range(1, len(rows)):
        # print(f"\ni={i}   {rows[i].text}")
        col = rows[i].find_elements_by_tag_name('td')

        tmp = []
        # [3]: duration
        tmp.append(re.findall(r'\d+', col[3].text))
        # print(re.findall(r'\d+', col[3].text))

        TTD_list.append(tmp)

    # as re.findall returns an additionaly nested list we remove one nest(?) with  itertools.chain
    TTD_list = list(itertools.chain(*TTD_list))

    # convert to seconds
    for i in range(len(TTD_list)):
        for j in range(len(TTD_list[i])):
            # days
            if len(TTD_list[i]) == 4 and j == 0:
                TTD_list[i][j+1] = int(TTD_list[i][j+1]) + (int(TTD_list[i][j]) * 24)
            # seconds
            elif j == len(TTD_list[i]) - 1:
                TTD_list[i] = TTD_list[i][j]
            # hours, minutes
            else:
                TTD_list[i][j+1] = int(TTD_list[i][j+1]) + (int(TTD_list[i][j]) * 60)

    return TTD_list

def get_merc_quests():

    # copy save file
    copy_savefile(_driver=driver_quests, _file_name='clickerHeroSave_generated.txt')    

    driver_quests.get('C:/Users/Sebastian/OneDrive/Dokumente/vscode-workspace/Python/pyautogui/merc_calc/merc_lister_files/saved_resource.html')
    
    try:        
        # wait for page to load
        WebDriverWait(driver_quests, 10).until(EC.presence_of_element_located((By.ID, 'savegame')))
        
        # write save game data to textfield
        savegame_box = driver_quests.find_element_by_id('savegame')
        savegame_box.click()
        savegame_box.send_keys(Keys.CONTROL + 'v')
        global copying
        copying = False

        # edit number of sets of quests
        quests = driver_quests.find_element_by_id('inputQuests')
        quests.click()
        quests.send_keys(Keys.BACK_SPACE, amount_quests)

        # find import button and click it
        import_button = driver_quests.find_element_by_tag_name('button')
        import_button.click()

        # find table with data
        quest_div = driver_quests.find_element_by_id('quest')
        table_body = quest_div.find_element_by_tag_name('tbody')
        rows = table_body.find_elements_by_tag_name('tr')

        quest_list = []
        
        # save table data
        # start with index 1 as row 0 is used as a header
        for i in range(len(rows)):
            # print(f"\ni={i}   {rows[i].text}")
            col = rows[i].find_elements_by_class_name('tsource')

            tmp = []
            for j in range(len(col)):
                # get number (duration) and text (type of quest) in one list
                tmp.append(re.findall(r'\d+|[a-zA-Z]+', col[j].text))
            
            # if tmp is not empty (= tsource was found), append it to the final list
            if col:
                quest_list.append(tmp)

    except Exception as e:
        print(e)
        
    finally:
        # close driver as this driver is only used in this function
        driver_quests.close()
    
    
    return quest_list

def start_quest(quest_selection, TTD_list, _merc_index):
    # TODO write better "java"-doc for this function
    """ starts a quest
    returns:    True if quest startet, False if not
    """
    print(f'Quest Selection: {quest_selection}')

    # search for quests with rubies as reward and save them
    potential_quests = []
    for i in range(len(quest_selection)):
        if 'Rubies' in quest_selection[i][1]:
            potential_quests.append(quest_selection[i])
        
    # check if we have ruby quests to choose
    if potential_quests:
        # sort potential_quests by quest length
        insertion_sort(potential_quests)
        # reverse order for descending quest length
        potential_quests.reverse()

        # cycle through quests and start the longest ruby quest we can
        for j in range(len(potential_quests)):
            # check if mercenary has enough time till death, add 60 seconds tolerance
            if TTD_list[_merc_index] > (int(potential_quests[j][0]) + 60):
                # click the mercenary
                pyautogui.click(coords[f'merc_{_merc_index}']['left'], coords[f'merc_{_merc_index}']['top'], duration=short_wait)

                # get index of the quest in the original quest_selection
                x = quest_selection.index(potential_quests[j])

                # click the correct quest and accept
                pyautogui.click(coords[f'quest_{x}']['left'], coords[f'quest_{x}']['top'], duration = short_wait)
                pyautogui.click(coords['quest_accept']['left'], coords['quest_accept']['top'], duration = short_wait)

                print(f'Started Quest: {potential_quests[j]} ({x}) on merc {_merc_index}.')

                # return True since we found a quest for this selection of quests
                return True

    # if not check if mercenary has enough time to die and chose the top-most quest (top one is always the shortest), add 60 seconds tolerance
    elif TTD_list[_merc_index] > int(quest_selection[0][0]) + 60:
        # click the correct mercenary
        pyautogui.click(coords[f'merc_{_merc_index}']['left'], coords[f'merc_{_merc_index}']['top'], duration = short_wait)
        # click the correct quest and accept
        pyautogui.click(coords[f'quest_0']['left'], coords[f'quest_0']['top'], duration = short_wait)
        pyautogui.click(coords['quest_accept']['left'], coords['quest_accept']['top'], duration = short_wait)

        print(f'Found no Ruby Quests, starting shortest Quest on merc {_merc_index}.')

        # started a quest, return True
        return True

    # print on console that no quest startet on mercenary number _merc_index, and also print the time to die in minutes
    print(f'No Quest startet for Mercenary {_merc_index}!\t Time To Die: {int(TTD_list[_merc_index]) /60} min.')
    # no quest startet, return False
    return False

# sorts a 2D list by the first ([0]) index
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = int(arr[i][0])           
        keyItem = list(arr[i])
        j = i - 1
        while j >= 0 and key < int(arr[j][0]):
            arr[j+1] = arr[j]
            arr[j] = keyItem
            j -= 1

def get_new_save():
    # copy save file
    copy_savefile('clickerHeroSave_generated.txt')

    driver.get('https://kepow.org/clickerheroes/')

    try:        
        # wait for page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'savedata')))
        
        # write save game data to textfield
        savegame_box = driver.find_element_by_id('savedata')
        savegame_box.click()
        savegame_box.send_keys(Keys.CONTROL + 'v')
        global copying
        copying = False

        # check best hero beyond 8.000
        best_hero_check = driver.find_element_by_id('wep8k')
        best_hero_check.click()

        # check copy to clipboard when clicked
        copy_if_selected = driver.find_element_by_id('copyancientlevels')
        copy_if_selected.click()

        # check display advanced config
        advanced_config = driver.find_element_by_id('displayadvancedconfiguration')
        advanced_config.click()

        # set playstyle to hybrid 
        playstyle_radio = driver.find_element_by_xpath("//input[@name='buildmode' and @value='hybrid']")
        playstyle_radio.click()

        # set fragsworth/siyalitas ratio to 1
        frag_siya_ratio = driver.find_element_by_css_selector("div.slider-handle.min-slider-handle.round")
        move = ActionChains(driver)
        move.click_and_hold(frag_siya_ratio).move_by_offset(40, 0).release().perform()

        # enable save game generation
        save_generation = driver.find_element_by_id('displaysavegamegeneration')
        save_generation.click()

        # press read save button
        read_save_button = driver.find_element_by_id('import')
        read_save_button.click()

        # click generated save data to copy
        generated_save = driver.find_element_by_id('generatedsavedata')
        # generated_save.click()
        save_text = generated_save.get_attribute('value')

        # write save to file
        f = open(f'{save_path}\{int(read_counter_txt())+1}_clickerHeroSave_generated.txt', 'w')
        f.write(save_text)
        f.close()
        # increment save counter
        increment_counter_txt()

    finally:
        # driver.close()
        pass
    
def import_save():
    # copy save file
    copy_savefile('clickerHeroSave_generated.txt')

    move_mouse_to_prim_monitor()

    # move to settings and click
    pyautogui.click(coords['options']['left'], coords['options']['top'], duration = short_wait)

    # move to import, click twice to select textarea that appears
    pyautogui.click(coords['import']['left'], coords['import']['top'], duration = short_wait)
    pyautogui.click(coords['import']['left'], coords['import']['top'], duration = short_wait)

    # paste save string
    with pyautogui.hold('ctrl'):
        pyautogui.press('v')
    global copying
    copying = False
    
    # press confirm, exit the pop up and exit options 
    pyautogui.click(coords['import_confirm']['left'], coords['import_confirm']['top'], duration = short_wait)
    pyautogui.click(coords['import_exit']['left'], coords['import_exit']['top'], duration = short_wait)
    pyautogui.click(coords['exit_options']['left'], coords['exit_options']['top'], duration = short_wait)
    
def get_timelapse_info():
    # copy save file
    copy_savefile('clickerHeroSave_generated.txt')

    driver.get(r'C:\Users\Sebastian\OneDrive\Dokumente\vscode-workspace\Python\pyautogui\timelapse_calc\timelapse_calc.html')

    try:
        # wait for page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'savegame')))

        # write save game data to textfield
        savegame_box = driver.find_element_by_id('savegame')
        # the following doesn't work with any webdriver because characters get lost, why???
        # savegame_box.send_keys(get_savefile())
        savegame_box.click()
        savegame_box.send_keys(Keys.CONTROL + 'v')
        global copying
        copying = False
        
        # press read save button
        read_save_button = driver.find_element_by_id('readSaveButton')
        read_save_button.click()

        # get table data
        table = driver.find_element_by_id('TimelapsesTable')
        table_body = table.find_element_by_tag_name('tbody')
        rows = table_body.find_elements_by_tag_name('tr')
        timelapse_list = []
        for i in range(len(rows)-1):
            # print(f"\ni={i}   {rows[i].text}")
            col = rows[i].find_elements_by_tag_name('td')

            tmp = []
            # [0]: duration
            tmp.append(re.findall(r'\d+', col[0].text)[0])
            # print(re.findall(r'\d+', col[0].text)[0])
            # [1]: hero
            tmp.append(re.findall(r'\D+', col[1].text)[0])
            # print(re.findall(r'\D+', col[1].text)[0])
            # [2]: level
            tmp.append(col[2].text.replace(".",""))
            # print(col[2].text.replace(".",""))
            # [3]: zone
            # TODO add zone info to table? maybe for later uses?

            timelapse_list.append(tmp)

    finally:
        # driver.close()
        pass

    return timelapse_list

def start_timelapse(_current_timelapse):
    """ Buys a timelapse with the duration of _current_timelapse[0]. All Windows ingame should be closed when calling this function.
    """
    move_mouse_to_prim_monitor()

    # click on shop
    pyautogui.click(coords['shop']['left'], coords['shop']['top'], duration = short_wait)

    # click on timelapses
    pyautogui.click(coords['timelapses']['left'], coords['timelapses']['top'], duration = short_wait)

    # click on the given timelapse
    pyautogui.click(coords[f'timelapse_{_current_timelapse[0]}']['left'], coords[f'timelapse_{_current_timelapse[0]}']['top'], duration = short_wait)
    
    # click confirm
    pyautogui.click(coords['timelapse_confirm']['left'], coords['timelapse_confirm']['top'], duration = short_wait)

    # wait to finish
    while (timelapse_finished := pyautogui.locateOnScreen(images['timelapse_finished'], grayscale=True, confidence=0.8)) == None:
        print('Waiting for Timelapse to complete...',  end='\r')
        time.sleep(0.5)
    # move mouse to main monitor in case we moved it manually while waiting for the game to load
    move_mouse_to_prim_monitor()
    pyautogui.click(timelapse_finished.left+120, timelapse_finished.top+40, duration = short_wait)

    # close timelapses and shop   
    pyautogui.click(coords['timelapse_close']['left'], coords['timelapse_close']['top'], duration = short_wait)
    pyautogui.click(coords['shop_close']['left'], coords['shop_close']['top'], duration = short_wait)

# TODO einheitlich alle funktionen, die mit savefiles zu tun haben, den filename angeben (gerade sind manche mit .txt am ende und manche ohne), GLEICH NOCH DAZU KOMMENTIEREN!!
def copy_savefile(_file_name = 'clickerHeroSave.txt', _driver = driver):

    # wait if another thread/process is copying
    global copying
    while copying:
        print('Waiting for another copy to complete...',  end='\r')
        time.sleep(0.2)
    copying = True

    _driver.get(f'{save_path}\{read_counter_txt()}_{_file_name}')
    body = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    body.send_keys(Keys.CONTROL + 'a')
    body.send_keys(Keys.CONTROL + 'c')
    # driver.close()

# TODO change 'pre' and 'post' in calls
def save_game(_file_name, _fast_mode=False):    
    """ saves the game as '{read_counter_txt()}_{_file_name}.txt'
    _fast_mode: if True, skips saving the file, so save file will only be in clipboard
    """
    # move cursor to main monitor
    move_mouse_to_prim_monitor()

    # move to settings and click
    pyautogui.click(coords['options']['left'], coords['options']['top'], duration = short_wait)
    # move to save
    pyautogui.click(coords['save']['left'], coords['save']['top'], duration = short_wait)

    
    # cannot hardcode next stuff because window could move around
    # wait to let windows load
    while pyautogui.locateOnScreen(r"C:\Users\Sebastian\OneDrive\Dokumente\vscode-workspace\Python\pyautogui\windows.png", grayscale=True, confidence=0.8) == None:
        print('Waiting for Windows Save to load...',  end='\r')
        time.sleep(0.2)

    # do not save and exit the window if fast mode is on (_fast_mode == True)
    if _fast_mode:
        pyautogui.press('escape')
        
    else:
        # locate address bar and rightclick for options
        address_bar = pyautogui.locateOnScreen(r"C:\Users\Sebastian\OneDrive\Dokumente\vscode-workspace\Python\pyautogui\windows_1.png", grayscale=True, confidence=0.8)
        pyautogui.click(address_bar.left-50, address_bar.top+25, duration = short_wait, button='right')
        # click to edit address
        pyautogui.click(address_bar.left-50+14, address_bar.top+25+58, duration = short_wait)

        # edit path and enter
        pyautogui.write(save_path)   
        pyautogui.press('enter')
        
        # enter name of file
        save_button = pyautogui.locateOnScreen(r"C:\Users\Sebastian\OneDrive\Dokumente\vscode-workspace\Python\pyautogui\windows_2.png", grayscale=True, confidence=0.8)
        pyautogui.click(save_button.left, save_button.top-57, duration = short_wait)    
        if 'pre' in _file_name:
            pyautogui.write(f'{read_counter_txt()}_clickerHeroSave_PRE_ASC.txt')
        elif 'post' in _file_name:
            pyautogui.write(f'{read_counter_txt()}_clickerHeroSave.txt')
        else:
            pyautogui.write(f'{read_counter_txt()}_{_file_name}.txt')
        
        pyautogui.press('enter')

        time.sleep(0.5)
        if pyautogui.locateOnScreen(r"C:\Users\Sebastian\OneDrive\Dokumente\vscode-workspace\Python\pyautogui\save_confirmation.png", grayscale=True, confidence=0.8, region=(1027, 546, 1510, 785)) != None:
            pyautogui.press(['left', 'enter'])

    time.sleep(0.2)
    # exit settings    
    pyautogui.click(coords['exit_options']['left'], coords['exit_options']['top'], duration = short_wait)

def ascend():

    move_mouse_to_prim_monitor()
    
    # move and click ascension button
    pyautogui.click(coords['ascend']['left'], coords['ascend']['top'], duration = short_wait)

    # move mouse again to remove mouseover popup
    move_mouse_to_prim_monitor()

    # check for relic pop-up
    if pyautogui.locateOnScreen(images['ascend_relic_popup'], grayscale=True, confidence=0.8) != None:
        pyautogui.click(coords['ascend_relic_popup']['left'], coords['ascend_relic_popup']['top'], duration=short_wait)

    # confirm ascension
    pyautogui.click(coords['ascend_confirm']['left'], coords['ascend_confirm']['top'], duration = short_wait)
            
def move_mouse_to_prim_monitor():
    pyautogui.moveTo(1, 1, duration = short_wait)

def read_counter_txt():
    # check if file exists, if not create it
    fle = Path(f'{save_path}\_COUNTER.txt')
    fle.touch(exist_ok=True)

    f = open(fle, 'r')
    content = f.read()
    f.close()

    # check if string empty (=empty textfile)
    if not content: content = 0

    return content

# increment single number in textfile
def increment_counter_txt():
    content = read_counter_txt()
    
    count = int(content) + 1

    f = open(f'{save_path}\_COUNTER.txt', 'w')
    f.write(str(count))
    f.close()

    return count

def start_routine():  
    """ Gets the Clicker Heroes Window and maximizes it.
    """  
    # find the clicker heroes window, move it to the main monitor and maximize it
    ch_window = pyautogui.getWindowsWithTitle('Clicker Heroes')
    ch_window[0].moveTo(0, 0)
    # need to minimize it first, otherwise it can't maximize it (idk why)
    ch_window[0].minimize()
    ch_window[0].maximize()

    move_mouse_to_prim_monitor()

def click_same_looking_elements(_link, _i, _scroll_distance):
    """clicks all elements on screen that look like given image and then scrolls and clicks the other elements
    CUEEWNRLY ONLY FOR LEFT REGION

    :param link:            address to the image
    :param i:               iterations to perform
    :param scroll_distance: scroll distance (negative for down, positive for up)
    """

    # wait a bit and try to find image multiple times with waits in between
    tries = 0
    while (areas := pyautogui.locateOnScreen(_link, grayscale=True, confidence=0.7, region=regions['left']) == None) or tries > 20:
        time.sleep(0.4)
        tries += 1

    for i in range(_i):
        areas = list(pyautogui.locateAllOnScreen(_link, grayscale=True, confidence=0.7, region=regions['left']))
   
        # "uniquify" areas (remove coordinates that are too close together)
        j = 1
        while j < len(areas):
            level_up_smaller = (areas[j].top - 50) < areas[j-1].top
            level_up_equal = areas[j].top == areas[j-1].top
            if level_up_smaller or level_up_equal:
                areas.pop(j)
                j = j - 1
            j = j + 1
        
        # click each found area
        for j in range(len(areas)):
            pyautogui.click(areas[j].left, areas[j].top, duration = short_wait)

        # scroll
        pyautogui.scroll(_scroll_distance)
        # move mouse to top so mouse-over animations don't interfer with image recognition
        move_mouse_to_prim_monitor()
        time.sleep(med_wait)

def level_current_hero(_current_timelapse, _last_timelapse = None, _gild_new = True):
    """ Gilds and levels the hero located at _current_timelapse[1].
    """

    print(_current_timelapse)

    move_mouse_to_prim_monitor()
    
    # go to hero tab
    pyautogui.click(coords['tab_heroes']['left'], coords['tab_heroes']['top'], duration=short_wait)

    # scroll to bottom and wait for the game to catch up (scroll up first because game is buggy)
    # pyautogui.scroll(400)
    # pyautogui.scroll(-1000)
    pyautogui.click(coords['scroll_bottom']['left'], coords['scroll_bottom']['top'], duration = short_wait)
    time.sleep(0.3)    

    # gild current hero
    if _gild_new:
        # locate gild button
        gild_button = pyautogui.locateOnScreen(images['gilded'], grayscale=True, confidence=0.8, region=regions['left'])
        pyautogui.click(gild_button.left+50, gild_button.top+20, duration=short_wait)  
        # scroll down and wait for the game to catch up
        pyautogui.scroll(-2000)
        time.sleep(1)
        # locate current hero to gild
        # TODO write function that scans for image and waits for x seconds and tries again for y times
        gild_hero = pyautogui.locateOnScreen(images[f'gild_{str(_current_timelapse[1]).lower()}'], grayscale=True, confidence=0.7)
        with pyautogui.hold('q'):
            pyautogui.click(gild_hero.left+75, gild_hero.top+50, duration=short_wait)
        # close gilded tab
        # game bugs out when handled with this speed so need to click wherever remove mouseover popup    
        pyautogui.click(coords['gilded_close']['left']-100, coords['gilded_close']['top'], duration=short_wait)
        pyautogui.click(coords['gilded_close']['left'], coords['gilded_close']['top'], duration=short_wait)
        time.sleep(0.2)

    # locate current hero 
    # current_hero = pyautogui.locateOnScreen(images[f'gilded_{str(_current_timelapse[1]).lower()}'], grayscale=True, confidence=0.8, region=regions['left'])
    
    # level yachyil to max if yachiyl was last hero, because then we can buy the 10% damage buff from her
    if _last_timelapse and ('yachiyl' in _last_timelapse[1].lower()):
        # need to scroll to find her
        pyautogui.scroll(200)
        time.sleep(0.2)
        # locate yachyil in loop because image sometimes get resized and that always takes different time
        for i in range(40):        
            time.sleep(0.2)
            if (yachiyl := pyautogui.locateOnScreen(images[f'yachiyl'], grayscale=True, confidence=0.8, region=regions['left'])) != None:
                break
        # level yachiyl
        pyautogui.click(yachiyl.left-710, yachiyl.top+103, duration=short_wait, clicks=100)
        # scroll down again
        pyautogui.scroll(-400)
        time.sleep(1.8)

    # scroll up if last hero was dorothy and current hero is rose
    if _last_timelapse and ('dorothy' in _last_timelapse[1].lower()) and ('rose' in str(_current_timelapse[1]).lower()):
        pyautogui.scroll(200)
        time.sleep(0.2)

    # locate current hero in loop because image sometimes get resized and that always takes different time
    for i in range(40):
        time.sleep(0.2)
        if (current_hero := pyautogui.locateOnScreen(images[f'gilded_{str(_current_timelapse[1]).lower()}'], grayscale=True, confidence=0.8, region=regions['left'])) != None:
            break

    # assign auto clicker to current hero and hype-level it
    # with pyautogui.hold('c'):
    #     pyautogui.click(current_hero.left-710, current_hero.top+103, duration=short_wait)
    pyautogui.click(current_hero.left-710, current_hero.top+103, duration=short_wait, clicks=200)

    # buy available upgrades
    buy_upgrades()

def buy_upgrades():
    move_mouse_to_prim_monitor()

    # scroll to bottom
    pyautogui.click(coords['scroll_bottom']['left'], coords['scroll_bottom']['top'], duration = short_wait)
    time.sleep(0.5)
    
    # buy all upgrades
    buy_upgrades = pyautogui.locateOnScreen(images['buy_upgrades'], grayscale=True, confidence=0.8, region=regions['left'])
    pyautogui.click(buy_upgrades.left+190, buy_upgrades.top+40, duration = short_wait)

def play(_quest_list):
    time.sleep(0.5)
    move_mouse_to_prim_monitor()

    # enable progression mode
    pyautogui.write('a')
        
    # scroll to top and wait for the game to catch up
    pyautogui.click(coords['scroll_top']['left'], coords['scroll_top']['top'], duration = short_wait)
    time.sleep(0.75)

    # TODO refactor into own function? -> function is already done, just need to change this code to use the function instead
    click_same_looking_elements(r"C:\Users\Sebastian\OneDrive\Dokumente\vscode-workspace\Python\pyautogui\max_buy.png", 15, -200)

    # scroll to bottom just to be sure
    pyautogui.click(coords['scroll_bottom']['left'], coords['scroll_bottom']['top'], duration = short_wait)
    
    # buy all upgrades
    buy_upgrades = pyautogui.locateOnScreen(r"C:\Users\Sebastian\OneDrive\Dokumente\vscode-workspace\Python\pyautogui\buy_upgrades.png", grayscale=True, confidence=0.8, region=regions['left'])
    pyautogui.click(buy_upgrades.left+190, buy_upgrades.top+40, duration = short_wait)
    
    # # set auto clickers     
    # with pyautogui.hold('c'):
    #     pyautogui.click(coords['auto_clicker_spot']['left'], coords['auto_clicker_spot']['top'], clicks=amount_ACs-1)

    # get timelapse infos
    timelapse_info = get_timelapse_info()

    # get quests (we do this at the start of the program with multiprocessing since it takes a while and pass it to the play function)
    # quest_list = get_merc_quests()

    # for each timelapse
    # use x to organize skills and to compare with last timelapse inside the loop
    x = 0
    skills = ['5', '2', '4', '3', '7']
    for current_timelapse in timelapse_info:
                
        # activate an energized skill at index x, check if inside bounds first
        if x < len(skills):
            pyautogui.press(['8', skills[x]])
        # if not energize dark ritual
        else:
            pyautogui.press(['8', '6'])
        
        # click the mobs a bunch of times to generate some gold and collect it
        pyautogui.click(coords['auto_clicker_spot']['left'], coords['auto_clicker_spot']['top'], clicks=20)
        time.sleep(0.3)
        collect_gold()

        # manage current hero (gild and level it)
        # check if current hero is the same as last hero, check if it's not the first timelapse first to prevent out of bounds
        if x != 0 and current_timelapse[1] == timelapse_info[x-1][1]:
            # only pass _last_timelapse an argument if it's not the first timelapse, either when on high zone where yachiyl could
            # be the first hero to use and not maw we could get problems in level_current_hero()
            if x == 0:
                level_current_hero(current_timelapse, _gild_new=False)
            else:
                level_current_hero(current_timelapse, _last_timelapse=timelapse_info[x-1], _gild_new=False)
        else:
            level_current_hero(current_timelapse, _last_timelapse=timelapse_info[max(0, x-1)], _gild_new=True)

        # open mercenary tab
        pyautogui.click(coords['tab_merc']['left'], coords['tab_merc']['top'], duration = short_wait)
        time.sleep(2)

        # collect finished quests
        click_same_looking_elements(images['merc_collect'], 2, -400)

        # get to top of merc tab by clicking it
        pyautogui.click(coords['tab_merc']['left'], coords['tab_merc']['top'], duration = short_wait)
        manage_mercs(_quest_list, _fast_mode=True)

        # start timelapse
        start_timelapse(current_timelapse)

        # go back to hero tab
        pyautogui.click(coords['tab_heroes']['left'], coords['tab_heroes']['top'], duration = short_wait)

        # save game each step so we can get new merc infos
        save_game(_file_name='clickerHeroSave_generated', _fast_mode=True)

        # increment x
        x += 1

    # assign autoclickers
    with pyautogui.hold('c'):
        pyautogui.click(coords['auto_clicker_spot']['left'], coords['auto_clicker_spot']['top'], duration=short_wait, clicks=amount_ACs-1)

    # assign autoclicker to most current hero
    current_hero = (timelapse_info[len(timelapse_info) - 1][1]).lower()
    pyautogui.click((images[f'gilded_{current_hero}']['left']) - 710, (images[f'gilded_{current_hero}']['top']) + 103, duration=short_wait)
    
def collect_gold():
    for i in range(1737, 2136, 133):
        pyautogui.moveTo(i, 944, duration = short_wait)

if __name__ == "__main__":
    pyautogui.FAILSAFE = True

    # start a process to calculate quest list while we do other stuff
    pool = ThreadPool(processes=1)
    get_quests_process = pool.apply_async(get_merc_quests)

    print('start_routine')
    start_routine()

    print('save_game pre')
    save_game('pre')

    print('ascend')
    ascend()

    # save it as 'generated' because it's easier to just overwrite the file than to have another seperate file that's only used for generation
    print('save_game post')
    save_game('clickerHeroSave_generated')

    print('get_new_save')
    get_new_save()

    print('import_save')
    import_save()

    # wait for get_merc_quests() to finish
    print('Waiting for Quest List...')
    quest_list = get_quests_process.get()

    print('play')
    play(quest_list)

    # TODO get last skill of yachiyl (10% dps all heroes)
    # TODO edit timelapse spamming to only do x amount of timelapses or x amount of rubies?
    # TODO edit code to play every timelapse seperatly so we can stop/resume if an error happens or something else
    # TODO SOMEHOW NOT IMPORTING THE CORRECT GENERATED FILE

    # TODO only get TTD_list once and then just subtract the times