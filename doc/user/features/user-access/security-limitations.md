<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->
# Security Limitations

```{page-status} incomplete
:summary: This page needs to be restructured with Login into "login+security" and "secure storage" (2026/04)
```

## Credentials
An application may support sending emails or accessing data from a database. To
access those services, the application requires passwords.

APPXC does not expose those credentials in logging and, if configured
properly, only exposes them to admins. However, theoretically, the code
could be altered or the application rebuilt to extract them.

### Status Quo
Without additional efforts, access to a database would still be shared. It
would likely be shared directly, being available to others with the same
limitation as stated above. But will the exchange channel be secure? Will the
password be updated frequently? APPXC, at least, secures the communication path
*and* makes rolling out updated passwords seamless.

### Alternative - Individual Accounts
Wherever possible, individual accounts should be used! The credentials may be
maintained in APPXC but should be entered by the individual users. The
credentials should not be shared with others. There are a few scenarios where
this alternative is not applicable:
 * Service does not allow individual access or setup is high effort
 * Dynamic set of users and/or high number of users

### Alternative - Web Service
The only way to properly protect credentials is by not providing *direct*
access. A typical approach is to provide a web service with a user-specific login,
where users log in and the server handles the credentials. Such web-based services
will typically be too much effort for small-scale groups and might not be safer if:
* there are vulnerabilities in the web service, including all its exposed
  interfaces like the login procedure.
* there are vulnerabilities of the hosting server.

### Mitigation
* Check, if you need to share the credentials. Share only with the roles that
  really need it.
* Update passwords frequently! With APPXC you have a secure and convenient way
  to update them.

## Data
APPXC can share information securely to a selected group of users and even
retract this access again. However, users had once access to the data and could
have copied that data before retraction of access rights. They could also omit
any update by remaining offline or alter the application or build a new one to
keep the data access.

### Status Quo
Without APPXC, data would still be shared including the risk of users not
removing the data upon request.

### Alternatives
At the point where data must be shared, you cannot fully control how it will
be used.

### Mitigation
* Consider what data you need to share.
	* Consider the roles that need access.
	* Consider if a role needs access to all data or only part of it.
* Use APPXC capabilities to maintain and encrypt the data. Not only does this
  protect data from unauthorized access, it also adds a barrier for non-expert
  users.

## Conclusions
You are responsible for the security of the data you are handling. You need to
assess the sensitivity of your data and the attack surface you are providing.
Check the following:
1. Do you really have to exchange sensitive data?
2. If you need to exchange sensitive data, is your solution acceptable?
