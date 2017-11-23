# POP - a data downloader for the Stack Overflow API

## Usage

For a simple usage example, see `run.py`.

Initializing a `Period` object with start and end dates and telling it to
`pull()` the data will download a batch of questions from the API for the
given time frame. After downloading the questions, it will then look for
related data, such as answers, comments, tags and users. It will then
proceed to persist the data.

## Storage

By default, the data is persisted in the `output` directory. The application
is aware of the previous downloads that are stored in this directory, and
will not attempt to download them again.

## Credentials

The API's throttling limit can be greatly increased by providing the API
credentials. By default, they are stored in the `.key` and `.access_token`
files.
