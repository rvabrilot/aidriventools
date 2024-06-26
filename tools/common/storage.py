import pandas as pd
from floorer import Floorer

floorer = Floorer('storage/')

def store_transcriber(urls, landing, transcription, summary):
    """
    This function stores the transcriber output in the 'transcriber' folder in the 'storage' directory.

    Args:
        urls (str): The url of the video.
        landing (str): The folder where the video is stored.
        transcription (str): The transcription of the video.
        summary (str): The summary of the video.

    Returns:
        A string indicating the success or failure of the operation.
    """

    # Try Read a Parquet file
    msg = ""
    try:
        new_df = pd.DataFrame({'url': [urls], 'landing': [landing], 'transcription': [transcription], 'summary': [summary]})
        read_df = floorer.read_parquet('transcriber')
        combined = pd.merge(read_df, new_df, on='url', how='outer')
        combined_name = "transcriber"
        floorer.update_parquet(combined, combined_name)
        msg = "Transcriber updated successfully"
    except Exception as e:
        try:
            new_df = pd.DataFrame({'url': [urls], 'landing': [landing], 'transcription': [transcription], 'summary': [summary]})
            new_df_name = "transcriber"
            floorer.create_parquet(new_df, new_df_name)
            msg = "Transcriber created and stored successfully"
        except Exception as e:
            msg = "Error: " + str(e)
    finally:
        return msg
        
