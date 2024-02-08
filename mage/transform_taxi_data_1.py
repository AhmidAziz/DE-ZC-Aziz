if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd

@transformer
def transform(data, *args, **kwargs):
    # Specify your transformation logic here
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    col = {'VendorID':"vendor_id","RatecodeID":"rate_code_id","PULocationID":"pu_location_id","DOLocationID":"do_location_id"}
    data.rename(columns=col, inplace=True)
    filtered_df = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]
    return filtered_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with zero passengers'
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rides with zero trip_distance'
    assert output['vendor_id'].isin([1, 2]).all(), "There are rides vendor id not 1,2!"
