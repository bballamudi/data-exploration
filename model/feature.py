class Feature(object):
    def __init__(self, feat_name, feat_index, feat_datatype=None, feat_vartype=None, feat_count=None,
                 feat_missing=None, feat_unique=None, feat_average=None, feat_median=None, feat_mode=None,
                 feat_max=None, feat_min=None, feat_stddev=None, feat_variance=None, feat_skew=None, feat_kurtosis=None,
                 feat_quantile25=None, feat_quantile75=None, feat_iqr=None, feat_mostcommon=None, feat_leastcommon=None,
                 graph_histogram=None, graph_countplot=None, feat_errors=None, feat_warnings=None, feat_notes=None):
        # Feature stats
        self.feat_name = feat_name
        self.feat_index = feat_index
        self.feat_datatype = feat_datatype
        self.feat_vartype = feat_vartype
        self.feat_count = feat_count
        self.feat_missing = feat_missing
        self.feat_unique = feat_unique

        # Numeric only
        self.feat_average = feat_average
        self.feat_median = feat_median
        self.feat_mode = feat_mode
        self.feat_max = feat_max
        self.feat_min = feat_min
        self.feat_stddev = feat_stddev
        self.feat_variance = feat_variance
        self.feat_skew = feat_skew
        self.feat_kurtosis = feat_kurtosis
        self.feat_quantile_25 = feat_quantile25
        self.feat_quantile_75 = feat_quantile75
        self.feat_iqr = feat_iqr

        # Categorical only
        self.feat_mostcommon = feat_mostcommon
        self.feat_leastcommon = feat_leastcommon

        # Visualizations
        self.graph_histogram = graph_histogram
        self.graph_countplot = graph_countplot

        # Warnings, errors, and notes
        self.errors = feat_errors
        self.warnings = feat_warnings
        self.notes = feat_notes
