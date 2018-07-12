from google.cloud import storage
from time import strftime


CLIENT = storage.Client()


def create_bucket(bucket_name=''):
    """
    Create a bucket. The specified name must be globally unqiue to all of
    google cloud storage.
    ---
    See bucket naming requirements:
    `https://cloud.google.com/storage/docs/naming`
    """
    if not bucket_name:
        bucket_name = dummy_bucket_name()

    bucket = CLIENT.create_bucket(bucket_name)
    print(f"Cloud storage bucket `{bucket_name}` created.")
    return bucket_name


def dummy_bucket_name():
    ts = strftime("%Y-%m-%d_%H-%M-%S")
    return f"transcribe_bucket_{ts}"


# def delete_all_buckets():
#     """Delete all your buckets (to save $$$)"""
#     bucket_list = CLIENT.list_buckets()
#
#     for bucket in bucket_list:
#         bucket.delete()
#         print(f"Deleted bucket: `{bucket.name}`")


def delete_bucket(bucket_name):
    bucket = CLIENT.get_bucket(bucket_name)
    bucket.delete()
    print(f"Deleted bucket: `{bucket.name}`")


def upload_object(bucket_name, source_filepath, name=''):
    """
    Any file stored in google storage is called and object. Upload the
    specified file to the specified bucket and assign it a `name`.
    """
    if not name:
        name = source_filepath.split('/')[-1]

    bucket = CLIENT.get_bucket(bucket_name)
    blob = bucket.blob(name)
    blob.upload_from_filename(source_filepath)

    print(f"File {source_filepath}, named '{name}', uploaded to `{bucket_name}`.")
    return format_object_uri(bucket_name, name)


def list_objects(bucket_name):
    """What's in the bucket?"""
    bucket = CLIENT.get_bucket(bucket_name)
    blobs = bucket.list_blobs()                 # Returns a generator
    obj_names = [obj.name for obj in blobs]     # Exhausts the generator
    N = len(obj_names)

    if N == 0:
        print(f"Bucket `{bucket_name}` is empty.")
    else:
        s = "s" * (N > 1)
        print(f"Bucket `{bucket_name}` contains {N} file{s}:")
        for name in obj_names:
            print(name)

    return bucket.list_blobs()


def delete_all_objects_from_bucket(bucket_name):
    """Cannot be undone"""
    bucket = CLIENT.get_bucket(bucket_name)
    blobs = bucket.list_blobs()
    num_objs = len([blob.name for blob in blobs])
    if num_objs == 0:
        print(f"`{bucket.name} is empty.`")
    else:
        s = "s" * (num_objs > 1)
        print(f"From `{bucket.name}`, deleted object{s}:")
        for blob in bucket.list_blobs():
            blob.delete()
            print(f"`{blob.name}`")


def format_object_uri(bucket_name, obj_name):
    """
    All objects stored in google cloud storage has the following uri format:
    bucket name: `mybucket`
    object name: `myfile.csv`
    object uri:  `gs://mybucket/myfile.csv`
    """
    return f'gs://{bucket_name}/{obj_name}'


def upload_audio_files(filepaths, bucket_name=''):
    """
    bucket_name (str)
    filepaths (list of str)
    """
    bucket_name = create_bucket(bucket_name)
    uris = []
    for file in filepaths:
        gcs_uri = upload_object(bucket_name, file)
        uris.append(gcs_uri)
    return bucket_name, uris


def delete_everything(bucket_name):
    delete_all_objects_from_bucket(bucket_name)
    delete_bucket(bucket_name)


if __name__ == "__main__":
    print("Testing uploading to a bucket...")
    _ = create_bucket("dory")
    _ = upload_object("dory", "dentist_office.txt")
    _ = list_objects("dory")
    delete_all_objects_from_bucket("dory")
    delete_all_buckets()
    print("Test complete!")

    # bucket_name = "transcribe_bucket_2018-07-12_11-46-40"
    # delete_everything(bucket_name)
