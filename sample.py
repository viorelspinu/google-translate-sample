from google_cloud_service import GoogleCloudService

google_cloud_service = GoogleCloudService()

# language code from - https://cloud.google.com/translate/docs/languages
ret = google_cloud_service.do_translate_post("I am here", "ro")

print (ret)
