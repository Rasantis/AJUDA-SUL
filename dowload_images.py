from bing_image_downloader import downloader

search_term = input("Insira o termo de busca: ")
limit = int(input("Insira o limite de imagens: "))

downloader.download(search_term, limit=limit, output_dir='dataset2',
                    adult_filter_off=True, force_replace=False, timeout=60)