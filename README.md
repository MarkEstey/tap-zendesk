# tap-zendesk
A Singer tap for Zendesk, built with the Meltano SDK
`tap-zendesk` is a Singer tap for ZenDesk.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Installation

Install from GitHub:

```bash
pipx install git+https://github.com/MarkEstey/tap-zendesk.git
```

## Capabilities

* `catalog`
* `state`
* `discover`
* `about`
* `stream-maps`
* `schema-flattening`
* `batch`

## Settings

| Setting                  | Required | Default                   | Description |
|:-------------------------|:--------:|:-------------------------:|:------------|
| url_base                 | False    | https://zendesk.com       | Base url for the Zendesk API |
| email                    | True     | None                      | Email address used to log in |
| api_token                | False    | None                      | API token for the user |
| client_id                | False    | None                      | OAuth client ID |
| client_secret            | False    | None                      | OAuth client secret |
| incremental_request_rate | False    | 10                        | Maximum number of incremental requests per minute (see: https://developer.zendesk.com/api-reference/introduction/rate-limits/#endpoint-rate-limits) |
| start_date               | False    | 2007-09-01T00:00:00Z      | The earliest record date to sync |
| stream_type_conformance  | False    | root_only                 | The level of type conformance to apply to streams (see: https://sdk.meltano.com/en/latest/classes/singer_sdk.Stream.html#singer_sdk.Stream.TYPE_CONFORMANCE_LEVEL). Defaults to 'root_only'. Must be one of: 'none', 'root_only', 'recursive' |
| stream_maps              | False    | None                      | Inline stream maps (see: https://sdk.meltano.com/en/latest/stream_maps.html) |
| stream_map_config        | False    | None                      | Inline stream maps config (see: https://sdk.meltano.com/en/latest/stream_maps.html) |
| flattening_enabled       | False    | None                      | 'True' to enable schema flattening and automatically expand nested properties. |
| flattening_max_depth     | False    | None                      | The max depth to flatten schemas. |
| batch_config             | False    | None                      |             |

A full list of supported settings and capabilities for this tap is available by running:

```bash
tap-zendesk --about
```

### Configure using environment variables

This Singer tap will automatically import any environment variables within the working directory's
`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching
environment variable is set either in the terminal context or in the `.env` file.

### Source Authentication and Authorization

`tap-zendesk` uses API token authentication. See https://developer.zendesk.com/api-reference/introduction/security-and-auth/#api-token-deprecated and set `email` and `api_token`.

### Stream Type Conformance

This tap offers a configuration to control the level of record conformance to the schema. The default of `root_only` will validate the root level properties defined in the schema and checks that they are the appropriate type before passing the record to the target. This is useful for targets such as databases that expect a well-defined or consistent schema. If there are additional root level properties in the stream such as custom fields, you must configure them manually by adding them to the tap's schema with a validation type otherwise they will be excluded. However if the conformance level is to `none`, the tap does not validate the schema of records recieved from the source and passes them as-is to the target. This is useful for targets that are schemaless (such as `target-jsonl`) or in cases where you want to make sure all records and properties are captured even if the record does not follow the source schema.

## Usage

You can easily run `tap-zendesk` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-zendesk --version
tap-zendesk --help
tap-zendesk --config CONFIG --discover > ./catalog.json
```

## Developer Resources

Follow these instructions to contribute to this project.

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-zendesk
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-zendesk --version
# OR run a test pipeline:
meltano run tap-zendesk target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
