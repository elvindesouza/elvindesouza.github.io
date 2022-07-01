1. Keep all your secrets out of your repos. If you are using git, you can set up a .gitignore file for this. If you want to be super paranoid, put them in a completely different folder. If somebody gets a hold of your signing key, you are screwed.

2. If you are handling passwords, try to avoid handling them (seriously, it's a lot of responsibility to do it). If you have to, for the love of god make sure you use a strong hash and a salt. Never store passwords or other sensitive information (EG credit cards) in plain text.

3. Try to break your own software. I mean this quite literally. You know how it should work, but you need to constantly ask yourself "What if I do X?". The amount of weird bugs I have found by intentionally doing something I was not supposed to do in programs is amazing.

A subset of this is to try to break your own security. It can be somewhat hard to do though.

4. Be open to security audits. "I'm glad no one knows about this because it could probably get hacked very easily" is a terrible mindset to have. People should be able to look at your code and feel comfortable with what you have done. At the very least, write code as if you are going to be audited one day.

5. Never trust the user. The user should always be assumed to be malicious and because of point 3 is going to break everything. This means you should verify everything the user does is a valid thing for them to do.

An example of not doing this would be to create a password reset system with the following URL.

    http://<SITE>/resetpassword?userid=30&token=<TOKEN>

The problem with that is if you are only checking if they have a valid reset token, the user can just change the ID to any other user and reset their password, instead of their own. In this example each token should only be valid for a specific user.

6. A subset of 5 is to make sure you are not open to SQL injections. They will let people ruin and take control of your database.

7. Never trust your vendors. If you're using something that's from the public, you need to have a no trust policy with these products. The best ways to do this are things like running your own cache (such as sonatype's Nexus, or your own docker registry) or virus scanning on your images before they're used in production, among avoiding external dependencies when possible. It seems you hear once a month some docker image or npm package was being exploited.

8. Don't run things Public unless they're really supposed to be. If you're running your own registry or gitlab instance or Jenkins server, etc etc there usually isn't any reason to have it public. Utilize a VPN with key rotation to access your network and whitelist access to your tools appropriately within the VPN.

9. Don't use root accounts when you don't have to. This applies to almost anything, your local system, the user being run as inside a VM or docker, your AWS / Google cloud account, etc. By limiting use of root accounts you limit potentially how bad you'll be affected by an intrusion or vulnerability
