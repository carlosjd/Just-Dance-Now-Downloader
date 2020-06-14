print('JUST DANCE NOW DOWNLOADER BY CARLOS_')

import webbrowser

codename = input('Codename Gives Song : ')

jsonorbundle = input('Do You Want to Download .json or Bundle.zip:  ')


bundlelink = 'http://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/dist/bundle/' + codename + jsonorbundle

jsonlink = 'http://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/songs/' + codename + '/' + codename + jsonorbundle

if jsonorbundle == '.json':
    webbrowser.open(jsonlink)
else :
    webbrowser.open(bundlelink)

close = print('Finished')


