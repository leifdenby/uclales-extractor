from .object_types import CloudType

def present(ds, t0):
    """
    Return clouds that are present at time `t0`
    """
    # time of appearance
    tmin = ds.smcloudtmin
    # time of disappearance
    tmax = ds.smcloudtmax

    m = (tmin <= t0) & (t0 <= tmax)

    return m


def object_type(ds):
    return ds.object_type


def cloud_id(ds):
    return ds.smcloudid


def duration(ds):
    return ds.duration
