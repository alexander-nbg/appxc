<!--Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)-->
<!--SPDX-License-Identifier: 0BSD-->
# Login and Local Encryption

:::{page-status} usable
:summary: further refinement is pending while content appears complete enough (2026/04)
:::

The application requires a password on startup to store or load encrypted data.

## Situation
Your application may handle sensitive information or maintain passwords for server access
in the [configuration](/user/features/configuration). Such information should be stored
securely.

Another addressed situation arises from your specific application features when they
need to be aware of the current user, for example, to fill in their name or utilize
their email address. This information should be collected at some point.

## Approach
When the application is started for the first time, the user will need to enter their
user details (like an email address) and a password. At this point, APPXC will generate
a symmetric key, enabling secure storage and store the user details accordingly.

Whenever the application is started afterwards, the user needs to enter their password
to unlock the secure storage and their user details.

Additions via other features:
 * [Registration](registration) and [data synchronization](data-synchronization) need to
   securely share information between users for which asymmetric key pairs are generated
   for signing and encryption in addition to the symmetric key.
 * The [configuration](/user/features/configuration) uses secure storage by default and
   the user details are realized as a predefined configuration section.
 * During the [registration procedure](registration), the admin also reviews the user
   information before it is entered in the [user registry](user-registry)

## Alternatives
### Operating System
You may have set up your operating system to store data securely and a password is
already required to enter the operating system. This has two flaws:
 * It is hard to guarantee that ***every user*** will have their operating system
   protected.
 * As soon as the file is copied elsewhere (the operating system may be attacked), the
   data is not protected anymore.

Please note the general APPXC [security
limitations](security-limitations)
