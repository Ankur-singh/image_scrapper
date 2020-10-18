import streamlit as st
import base64
from google_images_download import google_images_download

def get_link(content, keyword):
    b64 = base64.b64encode(content.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'''<div align=center style="margin:20px"> 
                <a download="{keyword}.txt" href="data:file/txt;base64,{b64}" style="display: block;
    width: 80%;
    height: 43px;
    background: green;
    padding: 10px;
    text-align: center;
    border-radius: 10px;
    color: white;
    font-weight: bold;
    line-height: 25px;">Download {keyword}.txt file</a>
             </div>'''
    return href

response = google_images_download.googleimagesdownload()

st.markdown('# Image URL Scraper 🕸')
st.markdown('Deep Learning (CNNs) models requires tonnes of images to train. Often the process of collecting images (for custom dataset) is not easy. Search engines like bing and google make it even difficult to scrap images.')
st.markdown('#### How-to use')
st.markdown('Search for the keyword on google, narrow down the search by adding more relevant keyword. Keep doing it until you don\'t get the exact images for your dataset, then copy and paste the keywords in the field 👇')
st.markdown('**Note:** You can only scrape 99 urls, at once. If you want to scrape more urls then refer [sample usage notebook](https://github.com/Ankur-singh/image_scrapper/blob/master/sample_usage.ipynb)😉')
st.markdown('')


left_column, right_column = st.beta_columns([2,1])
keyword = left_column.text_input('Keyword')
limit = right_column.number_input('Number of image urls',
                                   min_value=5, max_value=99, step=1)

if keyword:
    arguments = {"keywords":keyword, "limit":limit, "chromedriver": 'chromedriver', "silent_mode":True, "no_download":True}
    paths = response.download(arguments)
    
    content = '\n'.join(paths[0][keyword])
    href = get_link(content, keyword)
    st.markdown(href, unsafe_allow_html=True)
    
    st.markdown('#### Usage')
    st.markdown('\nYou can download and verify all the images using helper functions from fastai\'s vision module. Code Snippet 👇. Refer [docs](https://docs.fast.ai/tutorial.vision) for more.')

    code = '''
from fastai.vision.all import *

download_images('elephant', Path('elephant.txt'))
fns = get_image_files(Path('elephant'))
failed = verify_images(fns)
print(failed)'''
    st.code(code)
