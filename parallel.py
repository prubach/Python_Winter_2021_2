from pathlib import Path

from knotprot_download import get_proteins, download_link, time_it, setup_download_dir, create_thumbnail
from multiprocessing.pool import Pool
from functools import partial
from concurrent.futures.process import ProcessPoolExecutor

#print(get_proteins())
def run_seq(my_dir):
    for p in get_proteins():
        download_link(my_dir, p)


def run_multiprocessing(my_dir):
    proteins = get_proteins()
    download = partial(download_link, my_dir)
    with Pool(16) as pl:
        pl.map(download, proteins)

##### Thumbnails
def thumbnails_sequential():
    for image_path in Path('images').iterdir():
        print(image_path)
        create_thumbnail((256, 256), image_path)

def thumbnails_parallel():
    create_thumbs = partial(create_thumbnail, (256, 256))
    with ProcessPoolExecutor(max_workers=8) as executor:
        executor.map(create_thumbs, Path('images').iterdir())

my_dir = setup_download_dir()
#time_it(run_seq, my_dir)
time_it(run_multiprocessing, my_dir)
