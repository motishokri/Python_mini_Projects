import instaloader
ig = instaloader.Instaloader()
db = input("Enter Insta Username:")
ig.download_profile(db , profile_pic_only=True)

