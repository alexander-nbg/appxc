<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->
# Registration

```{page-status} incomplete
The feature is outlined but cannot be detailed without implementation (2026/04)
```

The **registration** procedure adds new users to the [user registry](user-registry) and
enables [data synchronization](data-synchronization).

## Situation
You want to work with others via an application and corresponding data shall be
exchanged securely. This involves several questions:

1. How do others notify you that they want to join?
1. Who allows others to join your application?
1. How do users learn about new users?
1. How is the secure communication channel initialized?

## Approach
The **registration** procedure requires an **admin instance** and the **user instance**
that wants to register. It comprises three steps.
```{plantuml} registration.puml
```
1. User generates a registration request as a file
	* contains user information (see [login](login)) including the user's public keys for
	signing and encrypting data
	* encrypted with the admin public key
	* sent to admin, typically via email
2. Admin reviews the registration request, updates the user database and generates a
   registration response as a file
	* user roles are set during review
	* can include sections of the [configuration](/user/features/configuration)
	typically, at least, including the credentials for the shared storage to exchange
	the user registry
	* response data is encrypted with the user's public key
	* sent back to the user, typically via email
3. User loads the registration response

Not highlighted in the diagram is the synchronization of the [user
registry](user-registry) and other files via [data
synchronization](data-synchronization), which is triggered..
* ..upon the last step of the registration to ensure the new user has access to all
  required data.
* ..upon the second step of the registration to share the updated user registry with
  existing users.
* ..every time on application startup for the user registry to ensure correct user
  permissions for any data synchronization during the session.

:::{admonition} Implementation Incomplete
:class: warning

The registration procedure is implemented, including a transfer of configuration data
but due to the missing data synchronization, there is ***no automatic synchronization of
the user registry***.

:::
