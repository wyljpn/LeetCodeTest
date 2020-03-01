class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        mail_set = set()

        for email in emails:
            local_name, domain_name = email.split('@')
            local_name = local_name.split('+')[0].replace('.', '')
            mail_set.add(local_name+'@'+domain_name)
        return len(mail_set)